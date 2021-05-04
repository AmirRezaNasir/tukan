from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(30, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل معتبر'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان متن خود'}),
        label='عنوان',
        validators=[
            validators.MaxLengthValidator(100, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'پیام شما'}),
        label='متن پیام'
    )
