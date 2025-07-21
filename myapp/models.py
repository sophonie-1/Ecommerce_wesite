from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    #stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    #we use this where no image provide to avoide error
    @property
    def imageUrl(self):
        try:
            url =self.image.url
        except:
            url =''
        return url
    
class Order(models.Model):
    # status_choices = (
    #     ('Pending', 'Pending'),
    #     ('Processing', 'Processing'),
    #     ('Completed', 'Completed'),
    #     ('Cancelled', 'Cancelled'),
    # )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL ,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    #status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    @property
    def total_price(self):
        return float(self.price) * float(self.quantity)
    
    def save(self, *args, **kwargs):
        if not self.price and self.product:
            self.price = self.product.price  # assumes Product model has `price` field
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Order Items'
    

    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address_line1= models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    # country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipping Address for Order {self.order.id} by {self.customer.user.username}"