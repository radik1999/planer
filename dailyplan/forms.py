from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    model = Task
    fields = '__all__'
