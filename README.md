# Food Delivery API (Python, Django & Django REST)
This project is a simple backend API for a food delivery company, built using Django and Django Rest Framework (DRF). The API handles user registration and login, menu management, and order placement, with role-based permissions for users.


## Database Design
Designing a database schema for a food delivery service requires careful planning to accommodate all the necessary entities and their relationships. Below is a high-level overview of the database design, including the main entities and their relationships:

Main Entities
User
Restaurant
MenuCategory
MenuItem
Modifier
Order
OrderItem
Delivery
Database Schema
1. User
id (Primary Key)
username (Unique)
password
first_name
last_name
email
role (Choices: customer, owner, employee)
phone_number
gender
location
city
country
2. Restaurant
id (Primary Key)
owner (ForeignKey to User)
name
phone_number
email
town
country
3. MenuCategory
id (Primary Key)
name
restaurant (ForeignKey to Restaurant)
4. MenuItem
id (Primary Key)
name
category (ForeignKey to MenuCategory)
restaurant (ForeignKey to Restaurant)
quantity (default=1)
price
discount (default=0)
5. Modifier
id (Primary Key)
name
menu_item (ForeignKey to MenuItem)
additional_price (default=0)
6. Order
id (Primary Key)
customer (ForeignKey to User, related_name='orders')
restaurant (ForeignKey to Restaurant)
status (Choices: pending, completed, cancelled)
payment_method (Choices: cash, card)
total_price
created_at (DateTime)
updated_at (DateTime)
7. OrderItem
id (Primary Key)
order (ForeignKey to Order, related_name='items')
menu_item (ForeignKey to MenuItem)
quantity
unit_price
8. Delivery
id (Primary Key)
order (OneToOneField to Order)
delivery_person (ForeignKey to User)
delivery_address
delivery_date (DateTime)
delivery_status (Choices: pending, in_progress, completed)
Relationships
User:

One-to-Many with Restaurant (owner).
One-to-Many with Order (customer).
One-to-Many with Delivery (delivery_person).
Restaurant:

One-to-Many with MenuCategory.
One-to-Many with MenuItem.
MenuCategory:

One-to-Many with MenuItem.
MenuItem:

One-to-Many with Modifier.
Order:

One-to-Many with OrderItem.
One-to-One with Delivery.


