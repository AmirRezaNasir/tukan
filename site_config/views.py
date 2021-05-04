from django.shortcuts import render
from .models import SiteSetting
# Create your views here.
def about_my(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'shop/about_page.html', context)