from rest_framework import serializers
from . models import Product, Category ,Cart, Order, User , Reviews
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
 
class CartSerializer(serializers.ModelSerializer)                :
    class Meta :
        model =Cart
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer) :
    class Meta:
        model= Order
        fields='__all__'
        
#class UserSerializer(serializers.ModelSerializer):
 #   class Meta :
   #     model=User
    #    fields='__all__'
    
class Registerserializer(serializers.ModelSerializer):   
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
    def create(self, validition_data):
            user=User.objects.create_user(
                username=validition_data['username'],
                email=validition_data['email'],
                password=validition_data['password']
            ) 
            return user

class Reviwesserilaizer(serializers.ModelSerializer):
    class Meta:
        model= Reviews
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at']
        read_only_fields = ['user']
        