from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Mass
from .forms import *
from django.views import generic
import datetime, time
import locale

# List of mass
def massYear(request):
    week=datetime.datetime.today().isocalendar()[1]
    nextWeek=week+1
    previousWeek=week-1
    MassWeek=Mass.objects.filter(day__week=week)
    MassWeek1=Mass.objects.filter(day__week=nextWeek)
    MassSunday=Mass.objects.filter(day__week=previousWeek, day__week_day=1)

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
    locale.setlocale(locale.LC_ALL, "pl_PL")
    freeDate=[]
    mass=None
    alert=''
    search=SearchForm(request.POST or None, request.FILES or None)
    if search.is_valid():
        search_id=search.cleaned_data['date']
        h=search.cleaned_data['hourList']
        try:
            mass=Mass.objects.get(day=search_id, startTime=h)
            for x in range (0, 30):
                for h in hours:
                    day=search_id+datetime.timedelta(days=x)
                    hour=h[1]
                    try:
                        Mass.objects.get(day=day, startTime=h)
                    except:
                        z=day.strftime('%d %B %Y')
                        date=z+' '+hour
                        freeDate.append(date)
            alert='Termin Zajęty'
        except Mass.DoesNotExist:
            mass=Mass.objects.create(day=search_id, startTime=h)
            return redirect(massList)

    context={
    'freeDate':freeDate,
    'alert':alert,
    'search':search,
    'mass':mass
    }

    return render(request, 'search_mass.html', context)

#Add New Mass
def massList(request):
    massList=Mass.objects.filter(intention=None)
    return render(request, 'mass_list.html', {'massList':massList})

def editMass(request, id):
    mass=get_object_or_404(Mass, pk=id)
    form=MassForm(request.POST or None, request.FILES or None, instance=mass)
    if form.is_valid():
        form.save()
        return redirect(massYear)
    return render(request, 'mass_form.html', {'form':form})

def deleteMass(request, id):
    mass=get_object_or_404(Mass, pk=id)
    mass.delete()
    return redirect(search)
