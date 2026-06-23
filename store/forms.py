from django import forms
from .models import Product

class product_form(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'category', 'price', 'stock_left', 'description', 'image']
        