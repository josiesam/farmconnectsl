from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Product, Transaction
from .forms import ProductForm, TransactionForm

# Create your views here.
class IndexView(View):
    def get(self, *arg, **kwargs):
        return redirect('marketplace:product_list') 



class ProductListView(ListView):
    model = Product
    template_name = 'marketplace/product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'marketplace/product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        product = get_object_or_404(queryset, uuid=uuid)
        
        return product


class ProductCreateView(CreateView):
    model = Product
    template_name = 'marketplace/product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context
    


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'marketplace/product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        product = get_object_or_404(queryset, uuid=uuid)
        
        return product


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'marketplace/product/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        product = get_object_or_404(queryset, uuid=uuid)
        
        return product


class TransactionListView(ListView):
    model = Transaction
    template_name = 'marketplace/transaction/transaction_list.html'
    context_object_name = 'transactions'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'marketplace/transaction/transaction_detail.html'
    context_object_name = 'transaction'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        transaction = get_object_or_404(queryset, uuid=uuid)
        
        return transaction


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'marketplace/transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction_list')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'marketplace/transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction_list')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        transaction = get_object_or_404(queryset, uuid=uuid)
        
        return transaction


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'marketplace/transaction/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(location='marketplace')
        return context


    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        uuid = self.kwargs['uuid']
        
        transaction = get_object_or_404(queryset, uuid=uuid)
        
        return transaction
