# Generated by Django 3.1.7 on 2021-04-28 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی\u200cپی')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ادرس')),
                ('short_explanation', models.TextField(default='', max_length=250, verbose_name='توضيح مختصر')),
                ('description', models.TextField(verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='عکس محصول')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='زمان به روز رساني')),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت')),
                ('b_language', models.CharField(choices=[('PYTHON_DJANGO', 'پايتون - جنگو'), ('PYTHON_FLASK', 'پايتون -فلسک'), ('PYTHON_OTHER_ITEMS', 'پايتون -باقي موارد'), ('PHP', 'پي اچ پي - لاراول'), ('PHP_OTHER_ITEMS', 'پي اچ پي - باقي موارد'), ('JAVASCRIPT_NODE', 'جاوا اسکريپت - نود جي اس '), ('JAVASCRIPT_REACT_NATIVE', 'جاوا اسکريپت - ريکت نتيو'), ('JAVASCRIPT_OTHER_ITEMS', 'جاوا اسکريپت - باقي موارد'), ('C_SH_ASP', 'سي شارپ - اي اس پي دات نت '), ('C_SH_OTHER_ITEMS', 'سي شارپ - باقي موارد'), ('GO', 'گو')], max_length=50, verbose_name='زبان سمت بک اند')),
                ('f_language', models.CharField(choices=[('JAVASCRIPT_ANGULAR', 'جاوا اسکريپت - انگولار'), ('JAVASCRIPT_REACT', 'جاوا اسکريپت - ريکت'), ('JAVASCRIPT_VUE', 'جاوا اسکريپت - ويو جي اس '), ('JAVASCRIPT_AURELIA', 'جاوا اسکريپت - ارليا'), ('JAVASCRIPT_EMBER', 'جاوا اسکريپت - امبر'), ('JAVASCRIPT_OTHER_ITEMS', 'جاوا اسکريپت - باقي موارد'), ('HTML & CSS', 'HTML & CSS')], max_length=50, verbose_name='زبان سمت فرانت اند ')),
                ('price', models.IntegerField(verbose_name='قيمت')),
                ('phone_number', models.IntegerField(verbose_name='شماره تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ايميل')),
                ('is_special', models.BooleanField(default=False, verbose_name='مقاله ویژه')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='products', to='shop.Category', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'verbose_name': 'افزودن',
                'verbose_name_plural': 'ليست پروژه ها ',
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='ProductHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ipaddress')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='shop.ProductHit', to='shop.IPAddress', verbose_name='بازدیدها'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='بدنه دیدگاه ')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product')),
            ],
            options={
                'ordering': ['status', '-created_on'],
            },
        ),
    ]
