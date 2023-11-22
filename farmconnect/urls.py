from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('account/', include('account.urls'), name='account'),
    path('marketplace', include('marketinfo.urls'), name='marketinfo'),
    path('marketplace/', include('marketplace.urls'), name='marketplace'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

