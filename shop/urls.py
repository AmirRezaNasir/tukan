from django.urls import path
from .views import ProductList,ProductDetail,CategoryList,AuthorList,ProductPreview
app_name = "shop"
urlpatterns =[
	path('',ProductList.as_view(),name="productList"),
	path('page/<int:page>', ProductList.as_view(), name="productList"),
	path('product/<slug:slug>',ProductDetail.as_view(),name="productDetail"),
	path('preview/<int:pk>', ProductPreview.as_view(), name="preview"),
	path('category/<slug:slug>/', CategoryList.as_view(), name="category"),
	path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
	path('author/<slug:username>', AuthorList.as_view(), name="author"),
	path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
	# path('search/', SearchList.as_view(), name="search"),
	# path('search/page/<int:page>', SearchList.as_view(), name="search"),

]