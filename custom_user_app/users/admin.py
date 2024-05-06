from django.contrib import admin
from .models import Info
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AdminSite(UserAdmin):
    list_display = ("email", "username", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Info, AdminSite)