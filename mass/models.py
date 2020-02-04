from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django import forms
from mass.choices import *
from django.contrib.auth.models import User

#Mass type model
class MassType(models.Model):
    massType=models.CharField(max_length=50)
    def __str__(self):
        return str(self.massType)
#Place model
class Places(models.Model):
    place=models.CharField(max_length=50)
    def __str__(self):
        return str(self.place)
# Mass model
class Mass(models.Model):
    day=models.DateField(verbose_name=u"Data:", null=True)
    startTime=models.TimeField(verbose_name=u"Godzina:")
    intention=models.TextField(verbose_name=u"Intencja:", blank=True, null=True, max_length=250, default='Wolny Termin')
    surname=models.CharField(verbose_name=u"Imię i Nazwisko:", max_length=50, null=True)
    email=models.EmailField(max_length=70,blank=True, null=True)
    priest=models.ForeignKey(User, verbose_name=u'Kapłan', blank=True, on_delete=models.PROTECT, null=True)
    place=models.ForeignKey(Places, verbose_name=u'Miejsce', on_delete=models.CASCADE, null=True, blank=True)
    type=models.ForeignKey(MassType, verbose_name=u'Typ', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['day', 'startTime']

# Confession model
class Confession(models.Model):
    date=models.DateField(verbose_name=u"Data:", null=True)
    startHour=models.TimeField(verbose_name=u'Godzina')
    endHour=models.TimeField(verbose_name=u'Godzina')
    priest=models.ManyToManyField(User, blank=True, unique_for_date='day')
