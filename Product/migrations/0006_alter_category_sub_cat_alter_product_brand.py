# Generated by Django 4.0 on 2022-01-13 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_alter_product_cat_id_alter_property_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cattocat', to='Product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
