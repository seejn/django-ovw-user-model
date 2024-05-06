from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Info
# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Info

class UserAdmin(UserAdmin):
    inlines = [ProfileInline]

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
    )
# unregister old user
admin.site.unregister(User)

# register new user
admin.site.register(User, UserAdmin)