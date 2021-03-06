from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView, DetailView
from account.mixins import AuthorAccessMixin
from .models import Product,Category,Comment
from .forms import CommentForm
from account.models import User
from django.db.models import Q
from cart.forms import UserNewCartForm

# Create your views here.
class ProductList(ListView):
	paginate_by = 2
	queryset = Product.objects.published()

class ProductDetail(DetailView):


	def get_object(self):
		slug = self.kwargs.get('slug')
		product = get_object_or_404(Product.objects.published(), slug=slug)


		ip_address = self.request.user.ip_address
		if ip_address not in product.hits.all():
			product.hits.add(ip_address)
		
		return product


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cart_form = UserNewCartForm(self.request.POST or None,initial={'product_id':self.object.id})
		context['cart_form']= cart_form
		context['comments'] = Comment.objects.filter(product=self.object,status=1)
		if self.request.user.is_authenticated:
			context['comment_form'] = CommentForm(instance=self.request.user)
		return context

	def post(self, request, *args, **kwargs):
		new_comment = Comment(body=request.POST.get('body'),name=self.request.user,product=self.get_object())
		new_comment.save()
		return self.get(self, request, *args, **kwargs)



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
	paginate_by = 2
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


class SearchList(ListView):
	paginate_by = 2
	template_name = 'shop/search_list.html'

	def get_queryset(self):
		search = self.request.GET.get('q')
		return Product.objects.filter(Q(description__icontains=search)| Q(f_language__icontains=search)| Q(b_language__icontains=search) | Q(title__icontains=search))


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')

		return context
