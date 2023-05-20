from django import forms
from .models import Coach
class Coachform(forms.ModelForm):
    class Meta :
        model = Coach
        fields="__all__"