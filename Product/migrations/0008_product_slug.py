# Generated by Django 4.0 on 2022-02-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
