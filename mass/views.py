from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mass
from .forms import MassForm
import datetime, time

# Lista zajętych terminów w roku bieżącym
def massYear(request):
    year=datetime.datetime.today().year
    nextYear=year+1
    MassYear=Mass.objects.filter(day__year=year)
    MassYear1=Mass.objects.filter(day__year=nextYear)
    return render(request, 'mass.html',{'MassYear':MassYear, 'MassYear1':MassYear1, 'year':year, 'nextYear':nextYear})



#Dodawanie mszy
def addMass(request):
    form=MassForm(request.POST or None, request.FILES or None,)
    if form.is_valid():
        form.save()
        return redirect(massYear)
    return render(request, 'mass_form.html', {'form':form})

#lista wolnych 366 dni do przodu
def availableMass(request):
    a = datetime.datetime.today()
    numdays = 366
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    for x in range (0, numdays):
        day=a+datetime.timedelta(days = x)
        if day.weekday() == 0:
            monday.append(day)
        elif day.weekday() == 1:
            tuesday.append(day)
        elif day.weekday() == 2:
            wednesday.append(day)
        elif day.weekday() == 3:
            thursday.append(day)
        elif day.weekday() == 4:
            friday.append(day)
        elif day.weekday() == 5:
            saturday.append(day)
        elif day.weekday() == 6:
            sunday.append(day)

    hours=['6:00', '18:00']
    return render(request, 'Available_Mass.html',{'hours':hours,
                                                    'monday':monday,
                                                    'tuesday':tuesday,
                                                    'wednesday':wednesday,
                                                    'thursday':thursday,
                                                    'friday':friday,
                                                    'saturday':saturday,
                                                    'sunday':sunday})
