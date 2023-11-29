from django.contrib import admin
from .models import Product, Transaction

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('crop', 'price', 'available_quantity', 'seller')
    list_filter = ('crop', 'seller')
    search_fields = ('crop__name', 'seller__user__username')

    def get_readonly_fields(self, request, obj=None):
        # Make 'environment' and 'market' read-only
        return ['environment', 'market'] if obj else []

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'product', 'quantity', 'total_price', 'transaction_date')
    list_filter = ('buyer', 'product__crop', 'transaction_date')
    search_fields = ('buyer__user__username', 'product__crop__name')

    def get_readonly_fields(self, request, obj=None):
        # Make 'total_price' read-only
        return ['total_price'] if obj else []
