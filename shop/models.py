from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings


User = settings.AUTH_USER_MODEL
# Create your models here.
class ProductManager(models.Manager):
	def published(self):
		return self.filter(status='p')

class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)


class Category(models.Model):
	# parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
	title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="پوزیشن")

	class Meta:
		verbose_name = "دسته‌بندی"
		verbose_name_plural = "دسته‌بندی ها"
		ordering = ['position']
	def __str__(self):
		return self.title
	objects = CategoryManager()



class Product(models.Model):
	B_LANGUAGE_CHOICES=(
		('PYTHON_DJANGO','پايتون - جنگو'),
		('PYTHON_FLASK','پايتون -فلسک'),
		('PYTHON_OTHER_ITEMS','پايتون -باقي موارد'),
		('PHP','پي اچ پي - لاراول'),
		('PHP_OTHER_ITEMS','پي اچ پي - باقي موارد'),
		('JAVASCRIPT_NODE','جاوا اسکريپت - نود جي اس '),
		('JAVASCRIPT_REACT_NATIVE','جاوا اسکريپت - ريکت نتيو'),
		('JAVASCRIPT_OTHER_ITEMS','جاوا اسکريپت - باقي موارد'),
		('C_SH_ASP','سي شارپ - اي اس پي دات نت '),
		('C_SH_OTHER_ITEMS','سي شارپ - باقي موارد'),
		('GO','گو'),
	)
	F_LANGUAGE_CHOICES=(
		('JAVASCRIPT_ANGULAR','جاوا اسکريپت - انگولار'),
		('JAVASCRIPT_REACT','جاوا اسکريپت - ريکت'),
		('JAVASCRIPT_VUE','جاوا اسکريپت - ويو جي اس '),
		('JAVASCRIPT_AURELIA','جاوا اسکريپت - ارليا'),
		('JAVASCRIPT_EMBER','جاوا اسکريپت - امبر'),
		('JAVASCRIPT_OTHER_ITEMS','جاوا اسکريپت - باقي موارد'),
		('HTML & CSS','HTML & CSS'),
	)
	STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "برگشت داده شده"), # back
	)
	author  =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='products', verbose_name="نویسنده")
	title  =  models.CharField(max_length=300,verbose_name='عنوان')
	slug  =  models.SlugField(max_length=100,unique=True,verbose_name='ادرس')#slug hamun link hast unique ham yani tekrari nabashe
	short_explanation  =  models.TextField(max_length=250,default='',verbose_name="توضيح مختصر")
	description  =  models.TextField(verbose_name='محتوا')
	thumbnail  =  models.ImageField(upload_to="images",verbose_name='عکس محصول')
	publish  =  models.DateTimeField(default = timezone.now,verbose_name='زمان انتشار')
	updated  =  models.DateTimeField(auto_now=True,verbose_name='زمان به روز رساني')
	status  =  models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
	b_language  =  models.CharField(max_length=50,choices=B_LANGUAGE_CHOICES,verbose_name="زبان سمت بک اند")
	category  =  models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="products")
	f_language  =  models.CharField(max_length=50,choices=F_LANGUAGE_CHOICES,verbose_name="زبان سمت فرانت اند ")
	price  =  models.IntegerField(verbose_name='قيمت')
	phone_number  =  models.IntegerField(verbose_name='شماره تلفن')
	email  =  models.EmailField(max_length=254,verbose_name='ايميل')
	is_special  =  models.BooleanField(default=False, verbose_name="مقاله ویژه")

	# hits = models.ManyToManyField(IPAddress,through="ArticleHit", blank=True, related_name="hits", verbose_name="بازدیدها")
	class Meta:
		verbose_name = "افزودن"
		verbose_name_plural = "ليست پروژه ها "
		ordering = ['-publish']
	def __str__(self):
		return self.title

	def Category_to_str(self):
		return ", ".join([category.title for category in self.category.active()])

	objects = ProductManager()

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='بدنه دیدگاه ')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['status','created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)