# Food Delivery API (Python, Django & Django REST)
This project is a simple backend API for a food delivery company, built using Django and Django Rest Framework (DRF). The API handles user registration and login, menu management, and order placement, with role-based permissions for users.

Food Delivery Service Database Schema
Entities and Relationships
User

Fields: id (PK), username, email, password_hash, role, created_at, updated_at
Relationships:

User (1) - (0..N) Restaurant (A user can own multiple restaurants)
User (1) - (0..N) Order (As a customer)
User (1) - (0..N) Delivery (As a delivery person)



Restaurant

Fields: id (PK), owner_id (FK to User), name, description, address, phone_number, cuisine_type, operating_hours, created_at, updated_at
Relationships:

Restaurant (1) - (0..N) MenuCategory
Restaurant (1) - (0..N) MenuItem
Restaurant (1) - (0..N) Order



MenuCategory

Fields: id (PK), restaurant_id (FK to Restaurant), name, description, created_at, updated_at
Relationships:

MenuCategory (1) - (0..N) MenuItem



MenuItem

Fields: id (PK), category_id (FK to MenuCategory), restaurant_id (FK to Restaurant), name, description, price, is_available, created_at, updated_at
Relationships:

MenuItem (1) - (0..N) Modifier



Modifier

Fields: id (PK), menu_item_id (FK to MenuItem), name, price, is_required, created_at, updated_at

Order

Fields: id (PK), customer_id (FK to User), restaurant_id (FK to Restaurant), status, total_amount, created_at, updated_at
Relationships:

Order (1) - (1..N) OrderItem
Order (1) - (0..1) Delivery



OrderItem

Fields: id (PK), order_id (FK to Order), menu_item_id (FK to MenuItem), quantity, unit_price, subtotal, created_at, updated_at
Relationships:

OrderItem (1) - (0..N) OrderItemModifier



OrderItemModifier

Fields: id (PK), order_item_id (FK to OrderItem), modifier_id (FK to Modifier), quantity, unit_price, subtotal, created_at, updated_at

Delivery

Fields: id (PK), order_id (FK to Order), delivery_person_id (FK to User), status, pickup_time, estimated_delivery_time, actual_delivery_time, created_at, updated_at



