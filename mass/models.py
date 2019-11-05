from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django import forms
from mass.choices import *

rodo='Rodo txt'
# Create your models here.
class Mass(models.Model):
    day=models.DateField(verbose_name=u"Data:")
    startTime=models.CharField(verbose_name=u"Godzina:", default=0, choices=hours, unique_for_date='day',max_length=50)
    intention=models.TextField(verbose_name=u"Intencja:", blank=True, null=True, max_length=250)
    surname=models.CharField(verbose_name=u"Imię i Nazwisko:", max_length=50)
    email=models.EmailField(max_length=70,blank=True, null=True)
    approve=models.CharField(default='Nie', verbose_name=u"Akceptacja:",choices=approv, max_length=50)
    class Meta:
        ordering = ['day', 'startTime']
