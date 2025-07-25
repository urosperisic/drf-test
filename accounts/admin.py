from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')

    readonly_fields = ('role',)

    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom Info', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
