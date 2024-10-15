from django.contrib import admin
from django.utils.text import slugify
from .models import Crop, CropEnvironment, CropEconomic, MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('crop_type', 'crop_variety', 'planting_date', 'harvest_date', 'yield_amount')
    list_filter = ('crop_type', 'planting_date', 'harvest_date')
    search_fields = ('crop_type', 'crop_variety', 'pest_incidence', 'disease_incidence')

@admin.register(CropEnvironment)
class CropEnvironmentAdmin(admin.ModelAdmin):
    list_display = ('crop', 'latitude', 'longitude', 'altitude', 'soil_type', 'temperature_max', 'temperature_min', 'precipitation')
    list_filter = ('crop', 'soil_type', 'temperature_max', 'temperature_min', 'precipitation')
    search_fields = ('crop__crop_type', 'soil_type')

@admin.register(CropEconomic)
class CropEconomicAdmin(admin.ModelAdmin):
    list_display = ('crop', 'environment', 'cost_of_inputs', 'revenue', 'profit_loss', 'quality_parameters_moisture_content', 'quality_parameters_grain_size')
    list_filter = ('crop', 'environment', 'revenue', 'profit_loss', 'quality_parameters_moisture_content')
    search_fields = ('crop__crop_type', 'environment__latitude', 'quality_parameters_grain_size')

@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_display = ('economic', 'price', 'date')
    list_filter = ('economic', 'date')
    search_fields = ('economic__crop__crop_type',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'location')

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('event', 'user_profile', 'is_registered')
    list_filter = ('event', 'is_registered')
    search_fields = ('event__title', 'user_profile__user__username')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title', 'author__user__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'date')
    list_filter = ('date',)
    search_fields = ('post__title', 'user__user__username')

@admin.register(UserSubmittedArticle)
class UserSubmittedArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'submission_date', 'is_approved')
    list_filter = ('submission_date', 'is_approved')
    search_fields = ('title', 'author__user__username')
