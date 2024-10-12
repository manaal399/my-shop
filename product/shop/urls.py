from django.contrib import admin
from django.urls import path
from .views import product_list,view_cart,remove_from_cart,add_to_cart
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',product_list,name='product_list'),
    path('view_cart/',view_cart,name='view_cart'),  
    path('makeup/',views.makeup,name='makeup'),
    path('remove_from_cart/<int:product_id>/',remove_from_cart,name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('promotion/',views.promotion,name='promotion'),
    
    
]

