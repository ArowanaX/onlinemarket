# Generated by Django 4.0 on 2022-01-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_usersession'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='browser',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usersession',
            name='device',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usersession',
            name='os',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
