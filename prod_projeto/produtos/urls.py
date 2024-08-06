#produtos urls.py
from django.urls import path
from . import views

app_name = 'produtos'  
urlpatterns = [
     path('', views.home, name='home'),  # Default home view
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'), 
]



