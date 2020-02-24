#from django.forms import ModelForm
from .models import *
#from flatpickr import DatePickerInput, TimePickerInput
from django import forms
from django.forms import ModelForm, TimeInput, CheckboxInput
from mass.choices import *
import datetime, time
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class MassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields=['intention', 'surname', 'email', 'priest', 'place', 'type']
        widgets={
            #'startTime':TimePickerInput(),
            }
class NewMassForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields=['day', 'startTime', 'intention', 'surname', 'email', 'priest', 'place', 'type']
        widgets={
            'day':DatePickerInput(),
            'startTime':TimePickerInput(),
            }

class SearchForm(forms.Form):
    month=forms.ChoiceField(label='Miesiąc', choices=month, initial=datetime.datetime.today().month)
    year=forms.IntegerField(label='Rok', min_value=2019,
        initial=datetime.datetime.today().isocalendar()[0])

class NewConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields=['date', 'startHour', 'endHour', 'priest']
        widgets={
            'startHour':TimePickerInput(),
            'endHour':TimePickerInput(),
            }
