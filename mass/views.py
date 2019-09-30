from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Mass
from .forms import *
from django.views import generic
import datetime, time


# List of mass
def massYear(request):
    week=datetime.datetime.today().isocalendar()[1]
    nextWeek=week+1
    previousWeek=week-1
    MassWeek=Mass.objects.filter(day__week=week)
    MassWeek1=Mass.objects.filter(day__week=nextWeek)
    MassSunday=Mass.objects.filter(day__week=previousWeek)

    context={
        'MassWeek':MassWeek,
        'MassWeek1':MassWeek1,
        'week':week,
        'nextWeek':nextWeek,
        'MassSunday':MassSunday
    }
    return render(request, 'mass.html', context)

#Search for available dates
def search(request):
    mass=None
    alert=''
    search=SearchForm(request.POST or None, request.FILES or None)
    if search.is_valid():
        search_id=search.cleaned_data['date']
        h=search.cleaned_data['hourList']
        try:
            mass=Mass.objects.get(day=search_id, startTime=h)
            alert='Termin Zajęty'
        except Mass.DoesNotExist:
            mass=Mass.objects.create(day=search_id, startTime=h)
    return render(request, 'search_mass.html', {'alert':alert, 'search':search, 'mass':mass})

#Add New Mass
def addMass(request, id):
    mass=get_object_or_404(Mass, pk=id)
    form=MassForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(massYear)
    return render(request, 'mass_form.html', {'form':form})

def reload(mday,hour):
    mass=Mass.objects.filter(day=mday, startTime=hour)
    alert='Termin Wolny'
    return render_to_response('reload.html', {'mass':mass, 'alert':alert})
