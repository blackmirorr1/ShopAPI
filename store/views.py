from urllib import request

from django.shortcuts import render
from django_filters import OrderingFilter
from django.contrib.auth.models import User 
from store.filters import ProductFilter
from . models import Category, Product, Cart, Order, User, Reviews
from . serializers import ProductSerializer, CategorySerializer, CartSerializer, OrderSerializer , Registerserializer, Reviwesserilaizer #UserSerializer
from rest_framework import viewsets , status ,decorators
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner
from .pagination import ProductPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from django.db.models import Count, Avg, Sum

from store import serializers


# Create your views here.

#FBV(function based view for Product)( GET, POST , PUT , DELETE )

@api_view(['POST','GET' ])

def Product_list_api(request):
    
    if request.method=='POST':
        serializers=ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data ,status=status.HTTP_201_CREATED)
        return Response(serializers.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='GET':
        product=Product.objects.all()
        serializers=ProductSerializer(product ,many=True)
        return Response(serializers.data ,status=status.HTTP_200_OK)
    
@api_view(['DELETE','PUT'])

def Product_delete_update_api(request, id):
      if request.method=='DELETE':
          Product.delete
          return Response(status=status.HTTP_404_NOT_FOUND)
        
      elif request.method=='PUT':
            product=Product.objects.get(id=id)
            serializers=ProductSerializer(product ,data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data , status=status.HTTP_200_OK)
            return Response(serializers.errors ,status=status.HTTP_400_BAD_REQUEST)
        
#CBV(class based view for Product)( GET, POST , PUT , DELETE )
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            return [AllowAny()]
        return[IsAuthenticated()]
 
 
#FBV(function based view for order)( GET, POST , PUT , DELETE )
@api_view(['POST','GET'])
def order_api(request):
    if request.method=='POST':
        serializers=OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='GET':
        order=Order.objects.all()
        serializers=OrderSerializer(order , many=True)
        return Response(serializers.data , status=status.HTTP_200_OK)
    
@api_view(['DELETE','PUT'])
def order_delete_update_api(request ,id):
    if request.method=='DELETE':
        Order.delete
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method=='PUT':
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#CBV(class based view for order)( GET, POST , PUT , DELETE )
class Orderviewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['status']
    ordering_fields = ['created_at']
    def get_premissions(self):
        if self.action=="list" or self.action=="create":
            return[IsAuthenticated()]
        return[IsOwner()]
    def perform_create(self, serializer): # ال def  دي عشان نبعت رساله ان المخزون او الاستوك خلص ولو موجود وتم الطلب بنقص الكميه من المخزون
     order = serializer.save(user=self.request.user)
     for product in order.products.all():
        if product.stock < 1:
            raise serializers.ValidationError(f'{product.name} is out of the stock')           
        product.stock -= 1
        product.save()
        
                
            
        
          

#FBV(function based view for Category)( GET, POST , PUT , DELETE )
@api_view(['POST','GET'])
def Category_api(request):
    if request.method=='GET':
        category=Category.objects.all()
        serializer=CategorySerializer(category, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#CBV(class based view for order)( GET, POST , PUT , DELETE )
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


#FBV(function based view for Cart)( GET, POST , PUT , DELETE )
@api_view(['POST','GET','DELETE'])
def Cart_api(request):
    if request.method=='GET':
        cart=Cart.objects.all()
        serializer=CartSerializer(cart, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        Cart.delete
        return Response(status=status.HTTP_404_NOT_FOUND)


#CBV(class based view for cart)( GET, POST , PUT , DELETE )
class CartViewsets(viewsets.ModelViewSet):
    
    serializer_class=CartSerializer  
    def get_permissions(self):
        return [IsAuthenticated(), IsOwner()]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    
    
    
    
# #FBV(function based view for user)( GET, POST , PUT , DELETE )      
# @api_view(['POST','GET','DELETE'])
# def User_api(request):
#     if request.method==('GET'):
#         user=user.objects.all()
#         serializer=UserSerializer(user, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
#     elif request.method==('POST'):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#     elif request.method==('DELETE'):
#         User.delete
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# CBV(class based view for user)( GET, POST , PUT , DELETE )
# class UserViewset(viewsets.ModelViewSet):
#         queryset=User.objects.all()
#        serializer_class=UserSerializer
   
#fbv for register
@api_view(['POST'])
def register_api(request):
    serializer=Registerserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)       

#cbv for register        
class registerview(CreateAPIView):
    queryset=User.objects.all( )   
    serializer_class=Registerserializer
    permission_classes=[AllowAny]        

#fbv for review
@api_view(['POST','GET'])
def Get_review_api(request):
    if request.method=="GET":
        queryset=Reviews.objects.all()
        serializer=Reviwesserilaizer(queryset, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer=Reviwesserilaizer(data=request.data)
        if serializer.is_valid():
             serializer.save(user=request.user) 
             return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#CBV for review
class ReviewViewset(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=request.user)    
    permission_classes = [IsAuthenticated]
    
    
    
@api_view(['GET'])
def statistics_api(request):
    total_sales = Order.objects.aggregate(Sum('total'))['total__sum']   #اجمالي المبيعات
    total_orders = Order.objects.count()    #اجمالي الاوردرات 
    avg_rating = Reviews.objects.aggregate(Avg('rating'))['rating__avg']  # متوسط الاراء 
    top_products = Product.objects.annotate(
        order_count=Count('order')
    ).order_by('-order_count')[:3]     # اعلي 3 منتجات مبيعا 
    
    return Response({
        'total_sales': total_sales,
        'total_orders': total_orders,
        'avg_rating': avg_rating,
        'top_products': ProductSerializer(top_products, many=True).data
    })
