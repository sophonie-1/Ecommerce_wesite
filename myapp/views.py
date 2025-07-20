from django.shortcuts import render
from .models import Product
# Create your views here.


def store_view(request):
    products =Product.objects.all()
    context={
        'products':products
    }   
    return render(request, 'myapp/store.html',context)

def cart_view(request):
    return render(request, 'myapp/cart.html')

def checkout_view(request):
    return render(request, 'myapp/checkout.html')