from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

from core.views import (
    AboutView, ContactView, HomeView,
    FAQView, TeamView, AffiliationView
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('account/', include('account.urls'), name='account'),
    path('marketinfo/', include('marketinfo.urls'), name='marketinfo'),
    path('marketplace/', include('marketplace.urls'), name='marketplace'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('team', TeamView.as_view(), name='team'),
    path('affiliation', AffiliationView.as_view(), name='affiliation'),
    path('faq', FAQView.as_view(), name='faq'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
