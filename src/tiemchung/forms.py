from django import forms
from django.forms import fields
from .models import Dan


class DanForm(forms.Form):
    cccd = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'dan',
        'placeholder': 'Căn cước công dân'
    }))
    ten = forms.CharField(label='Tên', max_length=50)


class DanModelForm(forms.ModelForm):
    class Meta:
        model = Dan
        fields = ['cccd', 'ten']
