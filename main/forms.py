
from django import forms
from django.forms import ModelForm, TextInput

from main.models import book

class ormForm(ModelForm):
    class Meta:
        model = book
        name = forms.CharField(label='name', max_length=5)
        author = forms.CharField(label='author', max_length=5)
        number = forms.CharField(initial='value field title')
        widgets = {  
            "qw": TextInput(attrs={
             "class":"form-control",
             "placeholder": "имя"
            }),
        }