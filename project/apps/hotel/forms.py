from django import forms
from . import models

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = models.TipoHabitacion
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = models.Habitacion
        fields = '__all__'
        widgets = {
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "precio_x_dia": forms.TextInput(attrs={"class": "form-control"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
            }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = models.Reserva
        fields = ['habitacion', 'fecha_entrada', 'fecha_salida']
        widgets = {
                "habitacion": forms.Select(attrs={"class": "form-control"}),
                "fecha_entrada": forms.DateInput(attrs={"class": "form-control", "placeholder": "DD/MM/YYYY"}),
                "fecha_salida": forms.DateInput(attrs={"class": "form-control", "placeholder": "DD/MM/YYYY"}),
        }

