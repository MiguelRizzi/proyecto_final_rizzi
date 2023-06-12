from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .forms import ReseñaForm
from .models import Reseña

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
    success_url = reverse_lazy("blog:index")
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ReseñaDelete(LoginRequiredMixin, DeleteView):
    model = Reseña
    success_url = reverse_lazy("blog:index")

class ReseñaUpdate(LoginRequiredMixin, UpdateView):
    model = Reseña
    success_url = reverse_lazy("blog:index")
    form_class = ReseñaForm
