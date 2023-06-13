from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Perfil
from django.contrib import messages

# Registro basado en funciones
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.user.is_staff:
            form = forms.UserStaffCreationForm(request.POST)
        else:
            form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, "Usuario creado correctamente.", extra_tags="alert alert-success")
            return redirect('home:index')
    else:
        if request.user.is_staff:
            form = forms.UserStaffCreationForm()
        else:
            form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})

# Views basadas en clases
class PerfilDetail(LoginRequiredMixin, DetailView):
    model = Perfil
    
class PerfilCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Informacion de perfil guardada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
   
    
class PerfilUpdate(LoginRequiredMixin, UpdateView):
    model= Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        messages.success(self.request, "Informacion de perfil actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
class PerfilDelete(LoginRequiredMixin, DeleteView):
    model= Perfil
    success_url = reverse_lazy("home:index")

    def get_success_url(self):
            messages.success(self.request, "Informacion de perfil eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()