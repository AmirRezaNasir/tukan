# Generated by Django 3.1.7 on 2021-04-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('about_us', models.TextField(blank=True, null=True, verbose_name='درباره ما')),
                ('copy_right', models.CharField(blank=True, max_length=200, null=True, verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
            },
        ),
    ]
