from django.db import models
from django.contrib.auth.models import User

# Create your models here
status=[
    ('pending','pending'),
    ('shipped','shipped'),
    ('delivered','delivered'),
]

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity} '
    
class Order(models.Model):
    user=models.ForeignKey('auth.User' ,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)    
    status=models.CharField(max_length=50 ,choices=status ,default='pending') 
    created_at=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=100,decimal_places=2)
    def __str__(self):
        return f'{self.user.username} - {self.status} - {self.total} '
    
#class User(models.Model):
 #   username=models.CharField(max_length=100)
  #  first_name=models.CharField(max_length=100)
   # middle_name=models.CharField(max_length=100)
    #last_name=models.CharField(max_length=100)
    #email=models.EmailField()    
    #password=models.CharField(("Password"), max_length=50)
    #def __str__(self):
    #    return self.username

class Reviews(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating} '


    
