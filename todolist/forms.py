
from django import forms
from django.forms import ModelForm
from . models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','desc']
