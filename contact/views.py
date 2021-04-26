from django.shortcuts import render ,redirect

from .models import ContactUs

# Create your views here.
from .forms import CreateContactForm


def contact_page(request):
	contact_form = CreateContactForm(request.POST or None)

	if contact_form.is_valid():
		new_contact = ContactUs(
			full_name = contact_form.cleaned_data.get('full_name'),
			email = contact_form.cleaned_data.get('email'),
			subject = contact_form.cleaned_data.get('subject'),
			text = contact_form.cleaned_data.get('text'),
			is_read = False
			)
		new_contact.save()
		return redirect("account:profile")


		# todo : show user a success message
	contact_form = CreateContactForm()


	context = {
		'contact_form': contact_form,
	}

	return render(request, 'contact_us/contact_us_page.html', context)
