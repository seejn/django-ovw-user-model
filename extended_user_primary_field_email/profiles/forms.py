from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Info


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Info
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Info
        fields = ("email",)