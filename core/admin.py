from django.contrib import admin
from .models import ContactUs, Team, Affiliation, FAQ

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'message')
    list_filter = ('user', 'subject')
    search_fields = ('user__user__username', 'subject')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'organization', 'role')
    list_filter = ('name', 'organization', 'role')
    search_fields = ('name', 'organization', 'role')

@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'logo')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('topic', 'question', 'answer')
    list_filter = ('topic',)
    search_fields = ('topic', 'question')
    
