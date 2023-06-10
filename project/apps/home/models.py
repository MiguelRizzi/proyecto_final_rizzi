from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    telefono = models.CharField(max_length=50 , null=True, blank=True)
    descripcion = models.TextField(max_length=250, null=True, blank=True)    

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):        
        return f'Usuario: {self.usuario.username}'
    
