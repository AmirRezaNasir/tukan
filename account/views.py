from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from shop.models import Product
from django.contrib.auth.views import LoginView , PasswordChangeView
from .models import User
from .forms import ProfileForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin
)






class HomeList(AuthorsAccessMixin, ListView):
	model = Product
	template_name = "registration/home.html"


	def get_queryset(self):
		if self.request.user.is_superuser:
			return Product.objects.all()
		else:
			return Product.objects.filter(author=self.request.user)


# Create your views here.


class ProductList(AuthorsAccessMixin, ListView):
	template_name = "registration/list.html"


	def get_queryset(self):
		if self.request.user.is_superuser:
			return Product.objects.all()
		else:
			return Product.objects.filter(author=self.request.user)


class ProductCreate(AuthorsAccessMixin,FormValidMixin,FieldsMixin,CreateView):
	model = Product
	template_name = "registration/product-create-update.html"
	success_url = reverse_lazy('account:list')


class ProductUpdate(AuthorAccessMixin,FormValidMixin,FieldsMixin,UpdateView):
	model = Product
	template_name = "registration/product-create-update.html"
	success_url = reverse_lazy('account:list')




class ProductDelete(SuperUserAccessMixin, DeleteView):
	model = Product
	success_url = reverse_lazy('account:list')
	template_name = "registration/product_confirm_delete.html"


class Profile(LoginRequiredMixin ,UpdateView):
	model = User
	template_name = "registration/profile.html"
	form_class = ProfileForm
	success_url = reverse_lazy("account:profile")

	def get_object(self):
		return User.objects.get(pk = self.request.user.pk)

	def get_form_kwargs(self):
		kwargs = super(Profile, self).get_form_kwargs()
		kwargs.update({
			'user': self.request.user
		})
		return kwargs


class Login(LoginView):
	def get_success_url(self):
		user = self.request.user

		if user.is_superuser or user.is_author:
			return reverse_lazy("account:home")
		else:
			return reverse_lazy("account:profile")


class PasswordChange(PasswordChangeView):
	success_url = reverse_lazy("account:password_change_done")
