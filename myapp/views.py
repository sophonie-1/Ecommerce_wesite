from django.shortcuts import render
from .models import Product,Customer, Order, OrderItem
from django.http import JsonResponse
import json
# Create your views here.


def store_view(request):
    products =Product.objects.all()
    context={
        'products':products
    }   
    return render(request, 'myapp/store.html',context)

def cart_view(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        
        
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(float(item.price) * float(item.quantity) for item in order_items)
        
             
    else:
        order_items = []
    context = {
        'order_items': order_items,
        'order': order if request.user.is_authenticated else None,
        'total_price': total_price if request.user.is_authenticated else 0,
        
    }
        
    return render(request, 'myapp/cart.html', context)

def checkout_view(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(float(item.price) * float(item.quantity) for item in order_items)
        
    else:
        order_items = []
    context = {
        'order_items': order_items,
        'order': order if request.user.is_authenticated else None,
        'total_price': total_price if request.user.is_authenticated else 0,
    }
    return render(request, 'myapp/checkout.html',context)


def updateCart(request):
    data = json.loads(request.body)
    
    product_id = data['productId']
    action = data['action']
    print('Action:', action)

    customer = Customer.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)

    order,created = Order.objects.get_or_create(customer=customer, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    
    
    
    

    return JsonResponse('Item was added', safe=False)