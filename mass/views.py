from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mass
from .forms import MassForm

# Create your views here.
def mass(request):
    #freeMass=Mass.objects.all()
    freeMass=Mass.objects.filter(day__year=2019)
    return render(request, 'mass.html',{'Mass2019':freeMass})

def addMass(request):
    form=MassForm(request.POST or None, request.FILES or None,)
    if form.is_valid():
        form.save()
        return redirect(mass)
    return render(request, 'mass_form.html', {'form':form})
