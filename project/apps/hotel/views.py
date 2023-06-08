from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models, forms 

# Create your views here.

class TipoHabitacionCreateView(LoginRequiredMixin, CreateView):
    model = models.TipoHabitacion
    form_class = forms.TipoHabitacionForm
    success_url = reverse_lazy("hotel:index")

class HabitacionCreateView(LoginRequiredMixin, CreateView):
    model = models.Habitacion
    form_class = forms.HabitacionForm
    success_url = reverse_lazy("hotel:index")


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = models.Reserva
    form_class = forms.ReservaForm
    success_url = reverse_lazy("hotel:index")

    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)

