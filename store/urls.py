from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import routers



router=routers.DefaultRouter()
router.register('product',views.ProductViewSet)
router.register('category',views.CategoryViewset)
router.register('order',views.Orderviewset)
router.register('cart', views.CartViewsets, basename='cart')
#router.register('user', views.UserViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('product/',views.Product_list_api),
    path('product/<int:id>/',views.Product_delete_update_api),
    path('order/',views.order_api),
    path('order/<int:id>/',views.order_delete_update_api),
    path('category/',views.Category_api),
    path('cart/',views.Cart_api),
    path('cart/<int:id>/', views.Cart_api),
    path('register/', views.registerview.as_view()),
    path('review/', views.Get_review_api),
    path('review/', views.Get_review_api),
    path('review/cbv/', views.ReviewViewset.as_view({'get': 'list', 'post': 'create'})),
    path('statistics/', views.statistics_api),

]




