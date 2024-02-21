from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class RegisterUserFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name',"last_name","username","email","password1","password2")



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)