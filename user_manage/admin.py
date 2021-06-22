from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomizedUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name',
                    'is_medic', 'is_staff', 'is_active', 'last_login']
    list_editable = ['first_name', 'last_name',
                    'is_medic', 'is_staff', 'is_active', 'last_login']

admin.site.register(User, CustomizedUserAdmin)