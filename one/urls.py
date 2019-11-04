from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home),
    path('products/', views.product_list),
    path('products/<int:id>/fin', views.cart_product),
    path('products/car', views.car),
    path('products/check', views.check_out),
    
]