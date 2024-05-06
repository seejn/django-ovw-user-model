from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager
# Create your models here.


class Info(AbstractBaseUser, PermissionMixin):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=100, null=True, blank=True)
    
    firtname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    dob = models.DateTimeField(null=True)
    address = models.charField(max_length=100, null=True)
    phone_number = models.CharField(max_length=25, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email