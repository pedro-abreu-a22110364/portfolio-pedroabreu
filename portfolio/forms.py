from django import forms
from django.forms import ModelForm
from .models import *


class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link'}),
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'texto'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Autor',
            'data': 'Data',
            'titulo': 'Título',
            'link': 'Link',
            'texto': 'Texto',
        }
