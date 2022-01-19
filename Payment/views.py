from cgi import print_directory
from django.shortcuts import render
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404 ,JsonResponse  
from django.contrib.auth.decorators import login_required
from Cart.models import History
from django.core.cache import caches
import json


@login_required(login_url="user/login")
def go_to_gateway_view(request,price_total):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = price_total
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse("payment:callback"))
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e






def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        history=History()
        history.customer=request.user
        redis_cache=caches['default']
        cart=redis_cache.client.get_client()
        my_cart=cart.hgetall(request.user.email)
        value,counter={},1
        for elm in my_cart:
            value[f"product{counter}"]=json.loads(my_cart[elm])
            print(value)
            for i in value:
                print(value[i])
                value[i].pop("csrfmiddlewaretoken")
                value[i].pop("id")
                value[i].pop("img")
                value[i].pop("amount")
                
            counter+=1
            cart.hdel(request.user.email,elm)
        
        history.factor=value
        history.save()
        
        return JsonResponse(value)

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")




factory = bankfactories.BankFactory()

# غیر فعال کردن رکورد های قدیمی
bank_models.Bank.objects.update_expire_records()

# مشخص کردن رکوردهایی که باید تعیین وضعیت شوند
for item in bank_models.Bank.objects.filter_return_from_bank():
	bank = factory.create(bank_type=item.bank_type, identifier=item.bank_choose_identifier)
	bank.verify(item.tracking_code)		
	bank_record = bank_models.Bank.objects.get(tracking_code=item.tracking_code)
	if bank_record.is_success:
		logging.debug("This record is verify now.", extra={'pk': bank_record.pk})