from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart,Cartitem,Category ,promotion
from django.db import models
from .models import promotion       

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = Cartitem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_item_count = count_cart_items(request)
    total = cart.total    
    return render(request, 'product/cart.html', {'cart_items': cart_items, 'total': total,'cart_item_count':cart_item_count})


def product_list(request):
    product = Product.objects.all()
    cart_item_count = count_cart_items(request)
    promot=promotion.objects.order_by('-id')[:3]
    return render(request, 'product/product_list.html', {'product': product,'cart_item_count':cart_item_count,'promotion':promot}) 
  
def count_cart_items(request):
    try:
        cart = Cart.objects.get(user=request.user)
        return cart.cartitem_set.aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0
    
def makeup(request):
    category=get_object_or_404(Category,name='makeup')
    product=Product.objects.filter(category=category)
    return render(request,'product/makeup.html',{ 'category':category,'product':product})

def remove_from_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    cart=Cart.objects.get(user=request.user)
    cart_item=Cartitem.objects.get(cart=cart,product=product)
    cart_item.delete()
    return redirect('view_cart') 
   


0 
