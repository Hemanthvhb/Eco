from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Capture input quantity from the POST request form data, default to 1
    qty_input = int(request.POST.get('quantity', 1))
    
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += qty_input
    else:
        cart_item.quantity = qty_input
        
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    # Ensure a cart model instance exists even if empty
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    # Safely look up the item belonging to this specific user's cart
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')  