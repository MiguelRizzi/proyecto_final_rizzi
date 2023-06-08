from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import forms

# Registro basado en funciones
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado correctamente."})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})

