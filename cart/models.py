from django.db import models
from account.models import User
from shop.models import Product

# Create your models here.


class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


    def __str__(self):
        return str(self.User)


    def get_total_price(self):
        amount = 0
        for detail in self.cartdetail_set.all():
            amount += detail.price * detail.count
        return amount

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(default=1,verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'
    def get_detail_sum(self):
        return self.count * self.price

        
    def __str__(self):
        return self.product.title
