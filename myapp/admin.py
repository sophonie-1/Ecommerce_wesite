from django.contrib import admin
from .models import CustomerProfile, Product, Order, OrderItem, ShippingAddress
# Register your models here.


admin.site.register([
    CustomerProfile,
    Product,
    Order,
    OrderItem,
    ShippingAddress
])