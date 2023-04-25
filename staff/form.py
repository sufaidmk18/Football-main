from django import forms
from .models import Staff,performance,Match,match_details
from django.forms.widgets import DateInput,TimeInput

class staffform(forms.ModelForm):
    class Meta :
        model = Staff
        fields="__all__"

class performanceform(forms.ModelForm):
    class Meta:
        model = performance
        exclude=["pname"]
import datetime

x = datetime.datetime(2020, 5, 17).date()
class Matchform(forms.ModelForm):
    class Meta:
        model = Match
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date","min":x}),
            'time':TimeInput(attrs={"type":"time"})
        }


class match_detailsform(forms.ModelForm):
    class Meta:
        model= match_details
        exclude=["Match"]
