# *# accounts/admin.py*
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     """Адмін клас для кастомного користувача"""
    
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
    
#     list_display = ["username", "email", "first_name", "last_name", 
#                    "is_available", "location", "is_staff", "is_active"]
    
#     list_filter = ["is_staff", "is_active", "is_available", "date_joined"]
    
#     fieldsets = UserAdmin.fieldsets + (
#         ('Додаткова інформація', {
#             'fields': ('bio', 'location', 'website', 'github_profile', 
#                       'linkedin_profile', 'hourly_rate', 'is_available', 'phone')
#         }),
#     )
    
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Додаткова інформація', {
#             'fields': ('email', 'first_name', 'last_name')
#         }),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)
