from django import forms
from.models import *
from django.forms.widgets import DateInput
from .models import manager

class Managerform(forms.ModelForm):
    class Meta :
        model = manager
        fields="__all__"