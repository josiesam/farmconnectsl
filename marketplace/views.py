from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, *arg, **kwargs):
        context = {}
        context.update(location='marketplace')
        return render(self.request, 'marketplace/index.html', context)
    

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Transaction
from .forms import ProductForm, TransactionForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'transactions'


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/transaction_detail.html'
    context_object_name = 'transaction'


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction_list')


class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction_list')


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')
