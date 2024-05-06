import django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email must be set")

        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.set_default("is_active", True)
        extra_fields.set_default("is_staff", True)
        extra_fields.set_default("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must be set True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must be set True")
            
        return self.create_user(email, password, **extra_fields)