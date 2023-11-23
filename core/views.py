from django.shortcuts import redirect, render
from django.views import View

class AboutView(View):
    def get(self, *args, **kwargs):
        return render(self.request,'core/about.html')

class ContactView(View):
        def get(self, *args, **kwargs):
             return render(self.request, "core/contact.html")
        