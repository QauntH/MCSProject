from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from mcshop import models

from mcuser.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):

    class Meta:
        model = models.User
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'address',
        ]

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.EmailField(required=False)
    phone_number = forms.IntegerField()
    address = forms.CharField()
