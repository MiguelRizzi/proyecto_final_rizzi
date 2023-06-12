from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['titulo', 'contenido', 'calificacion', 'imagen']
        widgets = {
        "titulo": forms.TextInput(attrs={"class": "form-control"}),
        "contenido": forms.Textarea(attrs={"class": "form-control"}),
        "calificacion": forms.Select(attrs={"class": "form-control"}),
        "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }