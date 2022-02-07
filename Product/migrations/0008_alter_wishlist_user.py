# Generated by Django 4.0 on 2022-01-30 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_userdevice_delete_usersession'),
        ('Product', '0007_alter_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlisttocustomer', to='User.profile'),
        ),
    ]
