from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'textarea', 'placeholder': 'Describe your task here', 'cols':30, 'rows':3}),
        }
