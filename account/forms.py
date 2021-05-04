from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import User

class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')

		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].help_text = None
		
		if not user.is_superuser:
			self.fields['username'].disabled = True
			self.fields['email'].disabled = True
			self.fields['special_user'].disabled = True
			self.fields['is_author'].disabled = True
			self.fields['phone_number'].disabled = True

	class Meta:
		model = User
		fields = ['username','notes','Education','location','skills','phone_number','email', 'first_name', 'last_name','special_user', 'is_author']




class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{11,11}$', message="شماره تلفن شما معتبر نیست ان را به درستی لطفا وارد کنید ، چرت و پرت پر نکن")
	phone_number = forms.CharField(validators=[phone_regex], max_length=11)
	class Meta:
		model = User
		fields = ('username', 'email','phone_number', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'placeholder': 'نام کاربری '})
		self.fields['email'].widget.attrs.update({'placeholder': 'ایمیل'})
		self.fields['phone_number'].widget.attrs.update({'placeholder': 'شماره تلفن '})
		self.fields['password1'].widget.attrs.update({'placeholder': ' گذرواژه'})
		self.fields['password2'].widget.attrs.update({'placeholder': ' تکرار گذرواژه'})