from django.forms import ModelForm
from django import forms
from .models import Converter

class ConvertForm(forms.ModelForm):
    link = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', widget=forms.TextInput(attrs={'placeholder': 'Вставьте ссылку'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите свой email'}))



    class Meta:
        model = Converter
        fields = '__all__'