from django.contrib import admin
from .models import Category,Product,Cart,Cartitem,promotion
# Register your models here.

admin.site.register(Category)   
admin.site.register(Product)                
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(promotion)
