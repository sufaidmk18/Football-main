from django import forms
from .models import player
class playerform(forms.ModelForm):
    class Meta :
        model = player
        fields="__all__"