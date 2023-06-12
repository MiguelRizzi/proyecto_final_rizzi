from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['titulo', 'contenido', 'calificacion', 'imagen']
        widgets = {
        "titulo": forms.TextInput(attrs={"class": "form-control"}),
        "contenido": forms.TextInput(attrs={"class": "form-control"}),
        "calificacion": forms.TextInput(attrs={"class": "form-control"}),
        "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }