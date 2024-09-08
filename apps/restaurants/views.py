from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from RestaurantAPI.permissions import IsOwnerOrEmployee
from rest_framework.authentication import TokenAuthentication
from .models import Restaurant, MenuCategory, MenuItem,Modifier
from .serializers import (RestaurantSerializer, MenuCategorySerializer, MenuItemSerializer,ModifierSerializer)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [TokenAuthentication]
    
    def get_permissions(self):
        """
        Return the permission classes based on the request method.
        """
        if self.request.method == 'POST':
            # Only admin users can create restaurants
            return [IsAdminUser()]
        else:
            # Any authenticated user can view the list or details
            return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new restaurant.
        """
        if not request.user.is_staff:
            return Response({"detail": "You do not have permission to create a restaurant."}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwnerOrEmployee]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwnerOrEmployee]



class ModifierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modifier.objects.all()
    serializer_class = ModifierSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrEmployee]