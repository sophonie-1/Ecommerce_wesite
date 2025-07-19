from django.shortcuts import render

# Create your views here.


def store_view(request):    
    return render(request, 'myapp/store.html')

def cart_view(request):
    return render(request, 'myapp/cart.html')

def checkout_view(request):
    return render(request, 'myapp/checkout.html')