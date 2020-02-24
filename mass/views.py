from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.views import generic

import datetime, time, calendar
import locale

from .models import *
from .forms import *
from .choices import *

# List of mass
def massYear(request):
    week=datetime.datetime.today().isocalendar()[1]
    year=datetime.datetime.today().isocalendar()[0]
    if week == 1:
        year=year-1
        previousWeek=datetime.datetime(year, 12, 28).isocalendar()[1]
    else:
        previousWeek=week-1

    sundayP = Mass.objects.filter(day__week=previousWeek, day__week_day=1)
    monday = Mass.objects.filter(day__week=week, day__week_day=2)
    tuesday = Mass.objects.filter(day__week=week, day__week_day=3)
    wednesday = Mass.objects.filter(day__week=week, day__week_day=4)
    thursday = Mass.objects.filter(day__week=week, day__week_day=5)
    friday = Mass.objects.filter(day__week=week, day__week_day=6)
    saturday = Mass.objects.filter(day__week=week, day__week_day=7)
    sunday = Mass.objects.filter(day__week=week, day__week_day=1)
    days=[sundayP, monday, tuesday, wednesday, thursday,  friday, saturday, sunday]
    context={
        'week':week,
        'days':days,
        'year':year,
    }
    return render(request, 'mass.html', context)

#Search for available dates
def search(request):
    locale.setlocale(locale.LC_ALL, "pl_PL")
    list=[]
    search=SearchForm(request.POST or None, request.FILES or None)
    if search.is_valid():
        month=int(search.cleaned_data['month'])
        year=int(search.cleaned_data['year'])
        for i in range (0, calendar.monthrange(year, month)[1]):
            for j in hours:
                date=datetime.datetime(year, month, i+1)
                time=j[1]
                mass=Mass.objects.get_or_create(day=date, startTime=time)
        list=Mass.objects.filter(day__year=year, day__month=month)
    context={
    'search':search,
    'list':list
    }
    return render(request, 'search_mass.html', context)

@login_required
def newMass(request):
    alert='Wszystko ok'
    form=NewMassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(massYear)

    context={
        'form':form,
        'alert':alert
    }
    return render(request, 'mass_form.html', context)

@login_required
def editMass(request, id):
    alert=''
    mass=get_object_or_404(Mass, pk=id)
    form=MassForm(request.POST or None, instance=mass)
    if form.is_valid():
        d=mass.day
        p=mass.priest
        mass=form.save(commit = False)
        if Mass.objects.filter(day=d, priest=p).exists():
            alert='Wybierz innego kapłana'
        else:
            mass.save()
            return redirect(massYear)
    return render(request, 'mass_form.html', {'form':form, 'alert':alert})

@login_required
def deleteMass(request, id):
    mass=get_object_or_404(Mass, pk=id)
    mass.delete()
    return redirect(massYear)

def confession(request):
    week=datetime.datetime.today().isocalendar()[1]
    year=datetime.datetime.today().isocalendar()[0]
    if week == 1:
        year=year-1
        previousWeek=datetime.datetime(year, 12, 28).isocalendar()[1]
    else:
        previousWeek=week-1
        sundayP = Confession.objects.filter(date__week=previousWeek, date__week_day=1)
        monday = Confession.objects.filter(date__week=week, date__week_day=2)
        tuesday = Confession.objects.filter(date__week=week, date__week_day=3)
        wednesday = Confession.objects.filter(date__week=week, date__week_day=4)
        thursday = Confession.objects.filter(date__week=week, date__week_day=5)
        friday = Confession.objects.filter(date__week=week, date__week_day=6)
        saturday = Confession.objects.filter(date__week=week, date__week_day=7)
        sunday = Confession.objects.filter(date__week=week, date__week_day=1)
        days=[sundayP, monday, tuesday, wednesday, thursday,  friday, saturday, sunday]
        context={
            'week':week,
            'days':days,
            'year':year,
        }
    return render(request, 'confession.html', context)

@login_required
def newConfession(request):
    alert='Wszystko ok'
    form=NewConfessionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(confession)

    context={
        'form':form,
        'alert':alert
    }
    return render(request, 'confession_form.html', context)
