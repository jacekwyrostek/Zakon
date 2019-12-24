#from django.forms import ModelForm
from .models import Mass
from flatpickr import DatePickerInput
from django import forms
from django.forms import ModelForm
from mass.choices import *
import datetime, time

class MassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields=['intention', 'surname', 'email', 'priest']

class SearchForm(forms.Form):
    month=forms.ChoiceField(label='Miesiąc', choices=month, initial=datetime.datetime.today().month)
    year=forms.IntegerField(label='Rok', min_value=2019,
    initial=datetime.datetime.today().isocalendar()[0])
