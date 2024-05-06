from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    dob = models.DateTimeField()
    address = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    phone_number = models.CharField(max_length=25)