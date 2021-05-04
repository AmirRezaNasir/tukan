from django.contrib.auth import views
from django.urls import path
from .views import (
	ProductList,
	HomeList,
	ProductCreate,
	ProductUpdate,
	ProductDelete,
	Profile,
	ProductComment,
	CommentUpdate,
)

app_name = 'account'

urlpatterns = [
	path('list', ProductList.as_view(), name="list"),
	path('comments', ProductComment.as_view(), name="comments"),
	path('update-comment/<int:pk>', CommentUpdate.as_view(), name="update-comment"),
	path('', HomeList.as_view(), name="home"),
	path('product/create', ProductCreate.as_view(), name="product-create"),
	path('product/update/<int:pk>', ProductUpdate.as_view(), name="product-update"),
	path('Product/delete/<int:pk>', ProductDelete.as_view(), name="product-delete"),
	path('profile/', Profile.as_view(), name="profile"),
]