# Generated by Django 3.1.7 on 2021-04-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='shop.IPAddress', verbose_name='بازدیدها'),
        ),
    ]