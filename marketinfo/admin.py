from django.contrib import admin

from .models import Crop, MarketPrice

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketPrice)
class MarketPrice(admin.ModelAdmin):
    pass
