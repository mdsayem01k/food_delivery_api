from django.contrib import admin
from apps.deliveries.models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'delivery_person', 'delivery_address', 'delivery_date', 'delivery_status']
    search_fields = ['delivery_address', 'delivery_status']
    list_filter = ['delivery_status', 'delivery_person']
