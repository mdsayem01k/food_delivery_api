from rest_framework.permissions import BasePermission

class IsOwnerOrEmployee(BasePermission):
    """
    Custom permission to only allow owners and employees to modify or add
    menu items and categories. All authenticated users can view them.
    """
    def has_permission(self, request, view):
        # Allow read permissions for any authenticated user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Allow modify permissions only for owners or employees
        return request.user.role in ['owner', 'employee']




class IsOwnerOrEmployeeOrCustomerReadOnly(BasePermission):
    """
    Custom permission to allow:
    - Owners and employees to view orders related to their own restaurant.
    - Customers can only view their own orders.
    - Any authenticated user can create orders.
    """
    def has_permission(self, request, view):
        # Allow POST for any authenticated user (for creating an order)
        if request.method == 'POST':
            return request.user.is_authenticated

        # Allow access to authenticated users for GET, HEAD, OPTIONS
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_authenticated

        # Deny access for non-authenticated users for non-read actions
        return False

    def has_object_permission(self, request, view, obj):
        # Customers can only access their own orders
        if request.user.role.lower() == 'customer':
            return obj.customer.user == request.user

        # Owners and employees can access orders only if related to their restaurant
        if request.user.role.lower() in ['owner', 'employee']:
            return obj.restaurant.owner == request.user or request.user in obj.restaurant.employees.all()

        # Superusers can access all orders
        if request.user.is_superuser:
            return True

        return False
    


class IsOwnerOrDeliveryPerson(BasePermission):
    """
    Custom permission to allow only restaurant owners to assign delivery persons
    and delivery persons to view their own deliveries.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        # Allow owners to assign delivery person to the order's restaurant they own
        if user.role == 'owner' and obj.order.restaurant.owner == user:
            return True

        # Allow delivery persons to see and update their own deliveries
        if user.role == 'deliveryman' and obj.delivery_person == user:
            return True
        
        return False