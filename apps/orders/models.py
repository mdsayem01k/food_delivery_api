from django.db import models
from apps.restaurants.models import MenuItem,Restaurant
from django.conf import settings

from django.db import models
from django.conf import settings

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('card', 'Card'),
        ('cash', 'Cash'),
    ]

    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES,default='cash')
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username} at {self.restaurant.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.id}"