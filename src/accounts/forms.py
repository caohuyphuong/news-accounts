from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active', ]
