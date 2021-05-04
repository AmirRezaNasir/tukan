from django import template
from ..models import Product , Category,Comment
from django.db.models import Count, Q
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def title():
    return "توکان"


@register.inclusion_tag("shop/partials/category_navbar.html")
def category_navbar():
	return {
		"category": Category.objects.filter(status=True)
	}


@register.inclusion_tag("shop/partials/sidebar.html")
def popular_products():
	last_month = datetime.today() - timedelta(days=30)
	return {
		"products": Product.objects.published().annotate(
			count=Count('hits', filter=Q(producthit__created__gt=last_month))
		).order_by('-count', '-publish')[:5],
		"title": "محصولات پربازدید ماه"
	}


@register.inclusion_tag("registration/partials/link.html")
def link(request,app_name, link_name, content, classes):
	return {
		"request": request,
		"link_name": link_name,
		"link": "{}:{}".format(app_name,link_name),
		"content": content,
		"classes": classes,
	}
