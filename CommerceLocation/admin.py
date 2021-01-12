from django.contrib import admin
from .models import CommerceLocation
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

@admin.register(CommerceLocation)
class CommerceLocation(OSMGeoAdmin):
    list_display = ('name', 'location')

