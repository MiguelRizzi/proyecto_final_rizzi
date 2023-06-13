from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class UserStaffCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(label="¿Es staff?", required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "is_staff"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar','telefono', 'descripcion']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={"class": "form-control"}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
