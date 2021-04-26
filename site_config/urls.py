from django.urls import path
from .views import about_my
app_name = "site_config"
urlpatterns =[
	path('', about_my, name="about_my"),

]