from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .forms import ReseñaForm
from .models import Reseña
from django.contrib import messages

# Create your views here.
class ReseñaDetail(LoginRequiredMixin, DetailView):
    model = Reseña

class ReseñaList(LoginRequiredMixin, ListView):
    model = Reseña
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = Reseña.objects.filter(autor__username__icontains=query)
        else:
            object_list = Reseña.objects.all()
        return object_list

class ReseñaCreateView(LoginRequiredMixin, CreateView):
    model = Reseña
    form_class = ReseñaForm
    success_url = reverse_lazy("blog:reseña_list")
    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Reseña creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
class ReseñaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reseña
    success_url = reverse_lazy("blog:reseña_list")
    form_class = ReseñaForm

    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario es el autor de la reseña, False de lo contrario."""
        reseña = self.get_object()
        return reseña.autor == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Reseña actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
class ReseñaDelete(LoginRequiredMixin, DeleteView):
    model = Reseña
    success_url = reverse_lazy("blog:reseña_list")

    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario es el autor de la reseña o si es miembro del staff. False de lo contrario."""
        reseña = self.get_object()
        return reseña.autor == self.request.user or self.request.user.is_staff
    
    def get_success_url(self):
            messages.success(self.request, "Reseña eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
