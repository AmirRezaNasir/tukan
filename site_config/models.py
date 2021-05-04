from django.db import models

# Create your models here.
class SiteSetting(models.Model):

    title = models.CharField(max_length=150, verbose_name='عنوان سایت')

    gitgub_address = models.URLField(default="www.example-gitgub-address.com",max_length = 200)

    insta_address = models.URLField(default="www.example-instagram-address.com",max_length = 200)
    
    tel_address = models.URLField(default="www.example-telegram-address.com",max_length = 200)

    email = models.EmailField(max_length=50, verbose_name='ایمیل')

    about_us = models.TextField(default="ASL",verbose_name='درباره من', null=True, blank=True,max_length=465)

    about_site = models.TextField(verbose_name='درباره سایت ', null=True, blank=True, max_length=465)
    copy_right = models.CharField(verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)


    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.title
