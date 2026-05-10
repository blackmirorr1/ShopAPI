# ShopAPI 🛒

E-Commerce REST API built with Django REST Framework as a learning project.
The API supports full shopping flow from browsing products to placing orders.

---

## Tech Used
- Python 3.13
- Django 5.2
- Django REST Framework
- JWT Authentication (SimpleJWT)
- django-filter

---

## Features
- Register & Login with JWT Tokens
- Products with Search, Filter by price, and Pagination
- Cart Management (each user sees only their cart)
- Orders with automatic Stock Management
- Reviews & Ratings (one review per product per user)
- Sales Statistics using Django ORM aggregations
- Custom Permissions (only owner can edit/delete their data)

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## API Endpoints

```
POST   /api/register/          → Create new account
POST   /api/token/             → Login and get JWT tokens
POST   /api/token/refresh/     → Refresh access token

GET    /api/product/           → List all products (with filter & search)
POST   /api/product/           → Add new product
PUT    /api/product/<id>/      → Update product
DELETE /api/product/<id>/      → Delete product

GET    /api/cart/              → View my cart
POST   /api/cart/              → Add item to cart
DELETE /api/cart/<id>/         → Remove item from cart

POST   /api/order/             → Place an order
GET    /api/order/             → View my orders

POST   /api/review/            → Add a review
GET    /api/review/            → View all reviews

GET    /api/statistics/        → View sales statistics (admin)
```

---

## Filter & Search

```
GET /api/product/?search=iphone
GET /api/product/?min_price=100&max_price=500
GET /api/product/?ordering=-price
GET /api/product/?page=2
```

---

Made by Mahmoud Mancy
