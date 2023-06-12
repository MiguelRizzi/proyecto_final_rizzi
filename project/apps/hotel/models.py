from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo de habitacion"
        verbose_name_plural = "Tipos de habitaciones"

    def __str__(self):
        return self.nombre
    
class Habitacion(models.Model):
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(unique=True)
    precio_x_dia = models.DecimalField(max_digits=10, decimal_places=2,)
    disponible = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="img/", null=True, blank=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return f"Habitacion N° {self.numero} - {self.tipo}"

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    precio_total  = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    class Meta:
        ordering = ("-fecha_entrada",)

    def clean(self):
        if self.habitacion.disponible == False:
            raise ValidationError("La habitacion no esta disponible")
        if self.fecha_entrada < timezone.now().date():
            raise ValidationError("La fecha de entrada no puede ser anterior al dia actual")
        if self.fecha_salida < timezone.now().date():
            raise ValidationError("La fecha de salida no puede ser anterior al dia actual")
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de entrada")
        
    def save(self, *args, **kwargs):
        """Guarda la instancia y calcula el precio total de la reserva segun numero de dias
        entre las fechas de entrada y salida.
        Establece a la habitacion de la reserva como no disponibe"""
        dias = (self.fecha_salida - self.fecha_entrada).days
        self.precio_total = self.habitacion.precio_x_dia * dias
        super().save(*args, **kwargs)
        self.habitacion.disponible = False
        self.habitacion.save()
        