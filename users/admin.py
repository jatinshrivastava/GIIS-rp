from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'student_name','user_type']
    fieldsets = (
        (('User'), {'fields': ('username', 'password','first_name','last_name', 'student_name','email','user_type','is_active','is_staff','is_superuser','last_login','date_joined','user_permissions')}),
    )
    pass
    
admin.site.register(CustomUser,CustomUserAdmin)