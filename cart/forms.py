from django import forms
from account.models import User


class UserNewCartForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )
