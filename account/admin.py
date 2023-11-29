from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'is_farmer', 'address')
    list_filter = ('is_farmer',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'address')

    def full_name(self, obj):
        return obj.full_name()
    full_name.short_description = 'Full Name'
