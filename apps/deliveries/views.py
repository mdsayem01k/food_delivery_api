from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Delivery
from .serializers import DeliverySerializer
from RestaurantAPI.permissions import IsOwnerOrDeliveryPerson

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrDeliveryPerson] 

    def get_queryset(self):
        user = self.request.user
        if user.role == 'owner':
            # Return only the deliveries of the restaurant owned by this user
            return Delivery.objects.filter(order__restaurant__owner=user)
        elif user.role == 'deliveryman':
            # Return only the deliveries assigned to this delivery person
            return Delivery.objects.filter(delivery_person=user)
        return Delivery.objects.none()

    def perform_update(self, serializer):
        # Only owners can assign a delivery person
        if self.request.user.role == 'owner':
            serializer.save()
