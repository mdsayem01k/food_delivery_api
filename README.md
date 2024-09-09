# Food Delivery API (Python, Django & Django REST)
This project is a simple backend API for a food delivery company, built using Django and Django Rest Framework (DRF). The API handles user registration and login, menu management, and order placement, with role-based permissions for users.


## Database Design
Designing a database schema for a food delivery service requires careful planning to accommodate all the necessary entities and their relationships. Below is a high-level overview of the database design, including the main entities and their relationships:

+-------------------+              +-------------------+
|      User         |              |    Restaurant     |
+-------------------+              +-------------------+
| id (PK)           |<--- Owner --->| id (PK)           |
| username          |              | owner_id (FK)     |
| role (Choices)    |              | ...               |
| ...               |              +-------------------+
+-------------------+                      |
       | 1                                   | 1
       |                                     |
       N                                     N
+-------------------+              +-------------------+
|  MenuCategory     |              |    MenuItem       |
+-------------------+              +-------------------+
| id (PK)           |              | id (PK)           |
| restaurant_id (FK)|              | category_id (FK)  |
| ...               |              | restaurant_id (FK)|
+-------------------+              | ...               |
                                    +-------------------+
                                               |
                                               | 1
                                               N
                                    +-------------------+
                                    |   Modifier        |
                                    +-------------------+
                                    | id (PK)           |
                                    | menu_item_id (FK) |
                                    | ...               |
                                    +-------------------+

+-------------------+              +-------------------+
|     Order         |<---Customer-->| Delivery          |
+-------------------+              +-------------------+
| id (PK)           |              | id (PK)           |
| customer_id (FK)  |              | order_id (FK)     |
| restaurant_id (FK)|              | delivery_person_id|
| ...               |              | ...               |
+-------------------+              +-------------------+



