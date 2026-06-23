from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Grabs your books (lotm, shadow slave, etc.) from the DB
    return render(request, 'store/product_list.html', {'products': products})