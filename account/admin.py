from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.fieldsets += (("فیلد های اختصاصی من ",
					 {'fields': ("is_author",
							"special_user",
							"Guest_user",
							"Free_user",
							"Important_user",
							"phone_number",
							"notes",
							"Education",
							"location",
							"skills")})),

UserAdmin.list_display += ('is_author', 'is_special_user','is_guest_user','Free_user','Important_user')


admin.site.register(User, UserAdmin)