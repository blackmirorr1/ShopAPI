from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Order, Cart, Reviews, User  # استورد الموديلات الخاصة بك هنا

# تسجيل الموديلات لتظهر في لوحة التحكم
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
#admin.site.register(User)
admin.site.register(Reviews)