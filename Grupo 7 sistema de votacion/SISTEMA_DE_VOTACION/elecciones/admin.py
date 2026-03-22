from django.contrib import admin
from .models import Eleccion

@admin.register(Eleccion)
class EleccionAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'fecha_inicio', 'fecha_cierre', 'estado']
    list_filter   = ['estado']
    list_editable = ['estado']