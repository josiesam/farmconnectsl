# urls.py
from django.urls import path
from .views import (
    IndexView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
)

app_name = 'marketplace'

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    
    # Product URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<uuid:uuid>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<uuid:uuid>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<uuid:uuid>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Transaction URLs
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/<uuid:uuid>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<uuid:uuid>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<uuid:uuid>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]
