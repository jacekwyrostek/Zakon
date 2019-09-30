from django.shortcuts import render
from .models import *
# Create your views here.
def news(request):
    news=News.objects.all()

    context={
    'news':news
    }

    return render(request, 'news.html', context)
