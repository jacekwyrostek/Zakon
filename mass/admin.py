from django.contrib import admin
from .models import Mass

# Register your models here.
@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display=('day', 'startTime', 'surname', 'approve')
    list_filter=('day', 'startTime', 'approve')
    search_fields=('day', 'startTime', 'surname')
