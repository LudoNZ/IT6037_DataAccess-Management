from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser
from .forms import CustomUserCreationForm, CustmoUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustmoUserChangeForm

    model = CustomUser

    list_display = [
        "username",
        "age",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", )}),)

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age", )}),)

admin.site.register(CustomUser, CustomUserAdmin),