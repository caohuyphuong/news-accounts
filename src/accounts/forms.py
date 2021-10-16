from django import forms
from django.contrib.auth import get_user_model
from django.forms import fields

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
