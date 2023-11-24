from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, *arg, **kwargs):
        context = {}
        context.update(location='marketplace')
        return render(self.request, 'marketplace/index.html', context)