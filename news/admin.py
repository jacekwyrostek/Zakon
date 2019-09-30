from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class MassAdmin(admin.ModelAdmin):
    list_display=('pubDate', 'title')
