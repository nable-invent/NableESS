from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# from rest_framework.authtoken.admin import TokenProxy
# Register your models here.
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email" , "profile_image", "first_name","last_name", "phone_number", "is_active", "date_joined", ] 
    search_fields = ["email", "first_name", "last_name", "phone_number",]
   
    fieldsets = (
        ('User Details', {'fields': ('email','password')}),
        ('Personal Details', {'fields': ('first_name', 'last_name', 'profile_image', 'phone_number',)}),
        ('Permission Info', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_active', 'is_superuser','groups', 'user_permissions', 'date_joined',)}
        )
    )
    
    add_fieldsets = (
        ('Personal Info', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'profile_image', 'phone_number', 'password1', 'password2')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ['groups', 'user_permissions']


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.unregister(TokenProxy)
