from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_title = "Hotel"
admin.site.site_header = "Hotel Admin"

@admin.register(models.TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    """
    - list_display: tupla que especifica los campos que se mostrarán en la lista de objetos
    - search_fields: tupla que especifica los campos por los que se puede buscar en la lista de objetos
    - list_filter: tupla que especifica los campos por los que se puede filtrar en la lista de objetos
    - ordering: tupla que especifica el orden en que se mostrarán los objetos
    """

    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = (
        "tipo",
        "numero",
        "precio_x_dia",
        "disponible",
        "imagen",
    )
    
    search_fields = ("tipo__nombre","numero",)
    list_filter = ("tipo__nombre",)
    ordering = (
        "tipo",
        "numero",
    )

@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "habitacion",
        "fecha_entrada",
        "fecha_salida",
        "precio_total",
    )
    
    search_fields = ("cliente__username", "habitacion__tipo__nombre")
    ordering = ("fecha_entrada",)
    list_filter = ("fecha_entrada",)
