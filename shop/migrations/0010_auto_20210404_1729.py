# Generated by Django 3.1.7 on 2021-04-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210404_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='بدنه دیدگاه '),
        ),
    ]