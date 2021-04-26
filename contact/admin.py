from django.contrib import admin

from .models import ContactUs
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ('full_name','subject','is_read')
	list_filter = ('is_read',)
	search_fields = ('subject', 'full_name')
	ordering = ['-is_read',]
	list_editable = ['is_read']
	
admin.site.register(ContactUs,ContactAdmin)
