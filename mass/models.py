from django.db import models
from datetime import date, datetime
from django.utils import timezone

rodo='Rodo txt'
# Create your models here.
class Mass(models.Model):
    hours={
        ('6:00','6:00'),
        ('9:00','9:00'),
        ('12:00','12:00'),
        ('18:00','18:00')
    }
    day=models.DateField(help_text='Data Mszy')
    startTime=models.CharField(default=0, choices=hours,max_length=50, unique_for_date='day', help_text='Godzina')
    intention=models.TextField(help_text='Intencja Mszy Św.', blank=True, null=True)
    surname=models.CharField(help_text='Imię i Nazwisko zamawiającego', max_length=50)
    email=models.EmailField(max_length=70,blank=True, null=True)
    approved=models.BooleanField(rodo)
    class Meta:
        ordering = ['day']
