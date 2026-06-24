from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class product_form(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'category', 'price', 'stock_left', 'description', 'image']
    

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)