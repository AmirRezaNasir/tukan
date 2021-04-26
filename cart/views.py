from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Cart ,CartDetail
from shop.models import Product
from .forms import UserNewCartForm
from django.http import HttpResponse
from zeep import Client
from django.utils import timezone

# Create your views here.

@login_required()
def add_user_cart(request):
	new_cart_form = UserNewCartForm(request.POST or None)
	if 'cart_form' in request.POST:
		if new_cart_form.is_valid():
			cart = Cart.objects.filter(User_id=request.user.id, is_paid=False).first()
			if cart is None:
				cart = Cart.objects.create(User_id=request.user.id, is_paid=False)

			product_id = new_cart_form.cleaned_data.get('product_id')
			count = new_cart_form.cleaned_data.get('count')
			if count <= 0:
				count = 1
			product = Product.objects.get_by_id(product_id=product_id)

			cart.cartdetail_set.create(product_id=product.id, price=product.price, count=count)
			# todo: redirect user to user panel
			# return redirect('/user/orders')
			return redirect("cart:user-cart")
	return redirect("shop:productDetail")


@login_required()
def user_open_cart(request):
    context = {
        'cart': None,
        'details': None,
        'total': 0

    }

    open_cart: Cart = Cart.objects.filter(User_id=request.user.id, is_paid=False).first()
    if open_cart is not None:
        context['cart'] = open_cart
        context['details'] = open_cart.cartdetail_set.all()
        context['total'] = open_cart.get_total_price()


    return render(request, 'registration/shopping-cart.html', context)


@login_required()
def remove_cart_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        cart_detail = CartDetail.objects.get_queryset().get(id=detail_id, cart__User_id=request.user.id)
        if cart_detail is not None:
            cart_detail.delete()
            return redirect("cart:user-cart")
    raise Http404('سبد خرید داری مومن ؟‌')


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09906475856'  # Optional

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/cart/verify'  # Important: need to edit for realy server.



def send_request(request):
    total_price = 0
    open_cart: Cart = Cart.objects.filter(is_paid=False, User_id=request.user.id).first()
    if open_cart is not None:
        total_price = open_cart.get_total_price()
        result = client.service.PaymentRequest(
            MERCHANT, total_price, description, email, mobile, f"{CallbackURL}/{open_cart.id}"
        )
    if result.Status == 100:
        return redirect('https://banktest.ir/gateway/zarinpal/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: test ' + str(result.Status))


def verify(request):
    cart_id = kwargs.get('cart_id')

    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_cart = Cart.objects.get_queryset().get(id=cart_id)
            user_cart.is_paid = True
            user_cart.payment_date = timezone.now()
            user_cart.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))#کد پیگیری
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
