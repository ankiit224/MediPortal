from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')}),
    )

admin.site.register(User, CustomUserAdmin)
