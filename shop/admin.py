from django.contrib import admin
from .models import Product,Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}
	list_editable = ['status']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('title','publish','author','status','slug','b_language','f_language','Category_to_str')
	list_filter = ('publish','status','b_language','f_language')
	search_fields = ('title', 'description','b_language','f_language')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-publish']
	list_editable = ['status']
	
	# actions = [make_published, make_draft]
admin.site.register(Product,ProductAdmin)


