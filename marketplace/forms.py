# forms.py
from django import forms
from django.forms import ModelForm
from account.models import UserProfile
from .models import Product, Transaction


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'available_quantity', 'seller']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'available_quantity': forms.NumberInput(attrs={'class': 'form-input'}),
            'seller': forms.Select(attrs={'class': 'form-select'}),
        }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['buyer', 'product', 'quantity', 'total_price']
        widgets = {
            'buyer': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-input'}),
        }
