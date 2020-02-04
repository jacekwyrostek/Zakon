from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display=('day', 'startTime', 'surname')
    list_filter=('day', 'startTime', 'priest')
    search_fields=('day', 'startTime', 'surname', 'priest')

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
        list_display=('place',)
        list_filter=('place',)

@admin.register(MassType)
class MassTypeAdmin(admin.ModelAdmin):
        list_display=('massType',)
        list_filter=('massType',)

@admin.register(Confession)
class ConfessionAdmin(admin.ModelAdmin):
        list_display=('date', 'startHour', 'endHour')
        list_filter=('date', 'startHour', 'endHour', 'priest')
