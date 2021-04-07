# Generated by Django 3.1.5 on 2021-03-05 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210305_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default='00000000000', validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='شماره تلفن'),
        ),
    ]