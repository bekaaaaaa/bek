from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Mate:
        model=User
        fields= ['Username', 'email', 'password1', 'password2']