from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView, DetailView
from account.mixins import AuthorAccessMixin
from .models import Product,Category
from account.models import User


# Create your views here.
class ProductList(ListView):
	paginate_by = 2
	queryset = Product.objects.published()

class ProductDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		product = get_object_or_404(Product.objects.published(), slug=slug)
		return product

class ProductPreview(AuthorAccessMixin, DetailView):
	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Product, pk=pk)


class CategoryList(ListView):
	paginate_by = 2
	template_name = 'shop/category_list.html'

	def get_queryset(self):
		global category
		slug = self.kwargs.get('slug')
		category = get_object_or_404(Category.objects.active(), slug=slug)
		return category.products.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context


class AuthorList(ListView):
	paginate_by = 5
	template_name = 'shop/author_list.html'

	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.products.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context


# class SearchList(ListView):
# 	paginate_by = 1
# 	template_name = 'blog/search_list.html'

# 	def get_queryset(self):
# 		search = self.request.GET.get('q')
# 		return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))


# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['search'] = self.request.GET.get('q')

# 		return context
