from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  
        
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}'s cart"
    
    @property
    def total(self):
        
        total = sum(item.total_price for item in self.cartitem_set.all())
        
        return total
    
class Cartitem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.cart.user.username}'s cart item"
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
class  promotion(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='promotions')
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return self.name

