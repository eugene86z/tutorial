from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import authenticate, get_user_model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User #goes to the User table
        fields = ['username', 'email', 'password']





class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']