from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from shop.models import Product ,Comment
from django.contrib.auth.views import LoginView , PasswordChangeView
from .models import User
from .forms import ProfileForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
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


class ProductComment(ListView):

	template_name = "registration/product_comments.html"

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Comment.objects.all()
		else:
			return Comment.objects.filter(product__author = self.request.user)

class CommentUpdate(UpdateView):
	model = Comment
	template_name = "registration/comment-update.html"
	fields = ('status',)
	success_url = reverse_lazy('account:comments')

	def form_valid(self,form):
		comment=form.save(commit=False)
		comment=self.status = True
		comment=form.save()
		return redirect("account:comments")






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




class Register(CreateView):
	form_class = SignupForm
	template_name = "registration/register.html"

	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = False
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = 'فعال سازی اکانت'
		message = render_to_string('registration/activate_account.html', {
			'user': user,
			'domain': current_site.domain,
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
		})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
					mail_subject, message, to=[to_email]
		)
		email.send()
		return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد.لطفا چک کردن قسمت هرزنامه ها فراموش نشود !  <a href="/login">ورود</a>')


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		return HttpResponse('اکانت شما با موفقیت فعال شد. برای ورود <a href="/login">کلیک</a> کنید.')
	else:
		return HttpResponse('لینک فعال سازی منقضی شده است. <a href="/registration">دوباره امتحان کنید.</a>')
