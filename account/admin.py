from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.fieldsets[2][1]['fields']=(
    'is_active',
    'is_staff',
    'groups',
    'user_permissions',
    'is_translator',
)
UserAdmin.list_display+=('is_translator',)
admin.site.register(User,UserAdmin)
