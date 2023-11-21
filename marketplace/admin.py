from django.contrib import admin

from .models import Product, Transaction
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    pass
