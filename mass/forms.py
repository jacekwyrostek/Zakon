#from django.forms import ModelForm
from .models import Mass
from flatpickr import DatePickerInput
from django import forms
from django.forms import ModelForm
from mass.choices import *

class MassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields=['day', 'startTime', 'intention', 'surname', 'email','approved']
        widgets = {
            'day': DatePickerInput(),
        }

class SearchForm(forms.Form):
    date=forms.DateField(label='Data', widget=DatePickerInput())
    hourList=forms.ChoiceField(label='Godzina', choices=hours)
