from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Use decorator to register CustomUser with CustomUserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add additional fields in admin
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Improve admin list view
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_of_birth')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
