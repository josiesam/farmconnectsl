from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, *arg, **kwargs):
        context = {}
        context.update(location='marketinfo')
        return render(self.request, 'marketinfo/index.html', context)
    
class EventsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='event')
        return render(self.request, 'marketinfo/events.html', context)
    
class BlogsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='blog')
        return render(self.request, 'marketinfo/blogs.html', context)
    
class TipsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='marketinfo')

        return render(self.request, 'marketinfo/tips.html', context)