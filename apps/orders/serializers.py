from django.db import transaction
from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.restaurants.models import MenuItem
from apps.users.models import Customer

class OrderSerializer(serializers.ModelSerializer):
    ordered_items = serializers.SerializerMethodField()
    order_cost = serializers.SerializerMethodField()
    customer_details = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = { 
            "customer": {"write_only": True},  
            "restaurant": {"write_only": True}, 
            "order_items": {"write_only": True},  
        }

    def get_restaurant_name(self, obj):
        return obj.restaurant.name if obj.restaurant else None

    def get_ordered_items(self, obj):
        return obj.items.values('menu_item__name', 'quantity', 'unit_price')

    def get_order_cost(self, obj):
        return sum([item.unit_price * item.quantity for item in obj.items.all()])

    def get_customer_details(self, obj):
        user = obj.customer.user
        customer = obj.customer
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "username": user.username,
            "role": user.role,
            "phone_number": customer.phone_number,
            "gender": customer.gender,
            "location": customer.location,
            "city": customer.city,
            "country": customer.country
        }

    @transaction.atomic
    def create(self, validated_data):
        order_items = validated_data.pop("order_items", [])
        customer = validated_data.pop("customer", None)
        restaurant = validated_data.pop("restaurant", None)
        
        # Get the authenticated user from context
        user = self.context.get("user")

        # Find or create a Customer object associated with the user
        customer, created = Customer.objects.get_or_create(user=user)

        # Create the Order object
        order = Order.objects.create(customer=customer, restaurant=restaurant, **validated_data)

        # Create the OrderItem objects
        order_item_objects = []
        for item in order_items:
            menu_item = MenuItem.objects.get(id=item["menu_item"])
            unit_price = menu_item.price * item["quantity"]
            discount = menu_item.discount or 0
            unit_price = menu_item.price

            order_item_objects.append(
                OrderItem(
                    order=order,
                    menu_item=menu_item,
                    quantity=item["quantity"],
                    unit_price=unit_price
                )
            )
        OrderItem.objects.bulk_create(order_item_objects)

        return order
