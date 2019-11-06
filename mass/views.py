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
    previousWeek=week-1

    sundayP = Mass.objects.filter(day__week=previousWeek, day__week_day=1, approve='Tak')
    monday = Mass.objects.filter(day__week=week, day__week_day=2, approve='Tak')
    tuesday = Mass.objects.filter(day__week=week, day__week_day=3, approve='Tak')
    wednesday = Mass.objects.filter(day__week=week, day__week_day=4, approve='Tak')
    thursday = Mass.objects.filter(day__week=week, day__week_day=5, approve='Tak')
    friday = Mass.objects.filter(day__week=week, day__week_day=6, approve='Tak')
    saturday = Mass.objects.filter(day__week=week, day__week_day=7, approve='Tak')
    sunday = Mass.objects.filter(day__week=week, day__week_day=1, approve='Tak')



    context={
        'week':week,
        'sundayP':sundayP,
        'monday':monday,
        'tuesday':tuesday,
        'wednesday':wednesday,
        'thursday':thursday,
        'friday':friday,
        'saturday':saturday,
        'sunday':sunday
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

        if search_id.weekday()!=6 and h=='09:00' or h=='12:00':
            alert='Niewłaściwa Godzina Wybierz 06:00 lub 18:00'
        else:
            try:
                mass=Mass.objects.get(day=search_id, startTime=h)
                a=0
                x=0
                while a < 5:
                    x+=1
                    for h in hours:
                        day=search_id+datetime.timedelta(days=x)
                        hour=h[1]
                        try:
                            Mass.objects.get(day=day, startTime=h)
                        except:
                            z=day.strftime('%d %B %Y')
                            date=z+' '+hour
                            freeDate.append(date)
                    a+=1
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

#List of mass without approved
def massApprove(request):
    massList=Mass.objects.filter(approve='Nie')
    return render(request, 'mass_approve.html', {'massList':massList})

#Admin edit mass
def massAdmin(request, id):
    mass=get_object_or_404(Mass, pk=id)
    mass.approve='Tak'
    mass.save()
    return redirect(massApprove)

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
