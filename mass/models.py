from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django import forms
from mass.choices import *
from django.contrib.auth.models import User

# Mass model
class Mass(models.Model):
    day=models.DateField(verbose_name=u"Data:", null=True)
    startTime=models.CharField(verbose_name=u"Godzina:", default=0, choices=hours, unique_for_date='day',max_length=50)
    intention=models.TextField(verbose_name=u"Intencja:", blank=True, null=True, max_length=250, default='Wolny Termin')
    surname=models.CharField(verbose_name=u"Imię i Nazwisko:", max_length=50, null=True)
    email=models.EmailField(max_length=70,blank=True, null=True)
    priest=models.ManyToManyField(User, blank=True)
    class Meta:
        ordering = ['day', 'startTime']
