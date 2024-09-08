from django.db import models
from django.conf import settings

class Delivery(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    delivery_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateTimeField()
    delivery_status = models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], max_length=20)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"