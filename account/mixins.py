from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from shop.models import Product

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields =["title","slug","short_explanation","description","thumbnail","publish","status","b_language","category","f_language","price"]
		if request.user.is_superuser:
			self.fields.extend(["author","phone_number","email"])
		return super().dispatch(request, *args, **kwargs)
# phone_number
# email

class FormValidMixin():
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
			self.obj.phone_number = self.request.user.phone_number
			self.obj.email = self.request.user.email
			if not self.obj.status == 'i':
				self.obj.status = 'd'
		return super().form_valid(form)

class AuthorAccessMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		product = get_object_or_404(Product, pk=pk)
		if product.author == request.user and product.email == request.user.email and product.phone_number == request.phone_number and product.status in ['b', 'd'] or\
		request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")


class SuperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")


class AuthorsAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser or request.user.is_author:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("account:profile")
		else:
			return redirect("account:login")