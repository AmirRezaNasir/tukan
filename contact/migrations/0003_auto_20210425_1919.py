# Generated by Django 3.1.7 on 2021-04-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210425_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='نام و نام خانوادگی'),
        ),
    ]
