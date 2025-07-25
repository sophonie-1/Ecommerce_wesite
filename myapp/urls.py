from django.urls import path
from .views import store_view, cart_view, checkout_view, updateCart

app_name = 'myapp'
urlpatterns = [
    path('', store_view, name='store'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('update-cart/', updateCart, name='update_cart'),
]