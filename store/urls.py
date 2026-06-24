from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ProductCreateView, product_list, unified_login_view, seller_dashboard,customer_register_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('login/', unified_login_view.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', customer_register_view.as_view(), name='customer_register'),

    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('dashboard/', seller_dashboard, name='seller_dashboard'), 
]