from .models import Order, OrderItem

def cart_context_processor(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(float(item.price) * float(item.quantity) for item in order_items)
        total_quantity = sum(item.quantity for item in order_items)
    else:
        order_items = []
        total_price = 0
        total_quantity = 0

    return {  
        'total_price': total_price,
        'total_quantity': total_quantity,
    }