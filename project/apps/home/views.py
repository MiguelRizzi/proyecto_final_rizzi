from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Perfil

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


class PerfilDetail(LoginRequiredMixin, DetailView):
    model = Perfil
    

class PerfilCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class PerfilUpdate(LoginRequiredMixin, UpdateView):
    model= Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy('home:index')

class PerfilDelete(LoginRequiredMixin, DeleteView):
    model= Perfil
    success_url = reverse_lazy("home:index")


