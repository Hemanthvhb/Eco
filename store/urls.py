from django.urls import path
from .views import ProductCreateView, product_list, unified_login_view, seller_dashboard

urlpatterns = [
    path('', product_list, name='product_list'),
    path('login/', unified_login_view.as_view(), name='login'),
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('dashboard/', seller_dashboard, name='seller_dashboard'), 
]