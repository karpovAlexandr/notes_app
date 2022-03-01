from django import forms
from django.contrib.auth.forms import UserCreationForm

from app_users.models import NoteUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = NoteUser
        fields = [
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "off"}
            ),
        }

