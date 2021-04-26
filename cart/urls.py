from django.urls import path

from .views import add_user_cart , user_open_cart ,send_request,verify,remove_cart_detail

app_name = "cart"

urlpatterns = [
    path('add-user-cart', add_user_cart,name="add-cart"),
    path('user-cart', user_open_cart,name="user-cart"),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
    path('remove-cart-detail/<detail_id>', remove_cart_detail,name="remove-cart"),

]
