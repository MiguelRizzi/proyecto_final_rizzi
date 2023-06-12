from django.contrib import admin
from .models import Reseña

# Register your models here.
@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "contenido",
        "autor",
        "calificacion",
        "imagen",
        "fecha",
    )
    search_fields = ("autor__username", "titulo")
    ordering = ("fecha",)
    list_filter = ("fecha",)