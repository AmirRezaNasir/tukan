from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)


# Create your models here.
class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name='ایمیل')
	notes  =  models.TextField(default='خوش باشيد' , max_length= 200,verbose_name='حرف براي گفتن')
	Education  =  models.TextField(default='خود پرورش داده شده ' , max_length= 200,verbose_name='تحصيلات')
	location  =  models.TextField(default='بدون ادرس' , max_length= 200,verbose_name='ادرس ')
	skills  =  models.TextField(verbose_name='مهارت ها ',default='نوشته نشده')
	phone_number  =  models.IntegerField(default='00000000000',validators=[MaxValueValidator(9999999999)], verbose_name='شماره تلفن')
	is_author  =  models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user  =  models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
	Guest_user  =  models.DateTimeField(default=one_day_hence, verbose_name="کاربر مهمان تا")
	Free_user  =   models.BooleanField(default=False, verbose_name="کاربر آزاد")
	Important_user  =   models.BooleanField(default=False, verbose_name="کاربر مهم ") #for activate comments


	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
	is_special_user.boolean = True
	is_special_user.short_description = "وضعیت کاربر ویژه"


	def is_guest_user(self):
		if self.Guest_user > timezone.now():
			return True
		else:
			return False
	is_guest_user.boolean = True
	is_guest_user.short_description = "وضعیت کاربر مهمان"


# توجه اسم بعضیاشونو با حروف بزرگ شروع کردم مثل کاربر مهمان که تاثیر داره