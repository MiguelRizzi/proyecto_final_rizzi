from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Habitacion(models.Model):
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(unique=True)
    precio_x_noche = models.DecimalField(max_digits=10, decimal_places=2,)
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"Habitacion N° {self.numero} - {self.tipo}"
    
class Reserva():
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(TipoHabitacion)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    

