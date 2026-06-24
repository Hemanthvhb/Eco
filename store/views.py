from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Product
from .forms import product_form,CustomerRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

class ProductCreateView(CreateView):
    model = Product
    form_class = product_form  
    template_name = 'store/add_product.html'  # Using your exact template name
    success_url = '/dashboard/'  
    login_url = 'login'  

class unified_login_view(LoginView):  # Using your exact class name
    template_name = 'store/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            return '/admin/'
        elif user.groups.filter(name='Sellers').exists(): 
            return '/dashboard/'
        else:
            return '/'

@login_required(login_url='login')
def seller_dashboard(request):
    books = Product.objects.all() 
    return render(request, 'store/seller_dashboard.html', {'books': books})

class customer_register_view(CreateView):
    model=User
    form_class=CustomerRegistrationForm
    template_name='store/register.html'
    success_url=reverse_lazy('login')