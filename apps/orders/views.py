from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from RestaurantAPI.permissions import IsOwnerOrEmployeeOrCustomerReadOnly


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrEmployeeOrCustomerReadOnly]

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_queryset(self):
        user = self.request.user

        # Customers can only see their own orders
        if user.role.lower() == "customer":
            return self.queryset.filter(customer__user=user)
        
        # Owners and employees can see orders for their own restaurant
        elif user.role.lower() in ["owner", "employee"]:
            return self.queryset.filter(restaurant__owner=user) | self.queryset.filter(restaurant__employees=user)

        # Superusers can see all orders
        elif user.is_superuser:
            return self.queryset
        
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        # Allow anyone (authenticated) to create an order
        return super().create(request, *args, **kwargs)
