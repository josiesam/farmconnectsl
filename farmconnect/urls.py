from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

from core.views import AboutView, ContactView


def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('account/', include('account.urls'), name='account'),
    path('marketplace/', include('marketinfo.urls'), name='marketinfo'),
    path('marketplace/', include('marketplace.urls'), name='marketplace'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)