

from rest_framework import serializers
from apps.deliveries.models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'order', 'delivery_person', 'delivery_address', 'delivery_date', 'delivery_status']
