from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models, forms 

# * Tipo de Habitacion

class TipoHabitacionDetail(DetailView):
    model = models.TipoHabitacion

class TipoHabitacionList(ListView):
    model = models.TipoHabitacion

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.TipoHabitacion.objects.filter(nombre__icontains=query)
        else:
            object_list = models.TipoHabitacion.objects.all()
        return object_list

class TipoHabitacionCreateView(LoginRequiredMixin, CreateView):
    model = models.TipoHabitacion
    form_class = forms.TipoHabitacionForm
    success_url = reverse_lazy("hotel:index")


class TipoHabitacionDelete(DeleteView):
    model = models.TipoHabitacion
    success_url = reverse_lazy("hotel:tipohabitacion_list")


class TipoHabitacionUpdate(UpdateView):
    model = models.TipoHabitacion
    success_url = reverse_lazy("hotel:tipohabitacion_list")
    form_class = forms.TipoHabitacionForm














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

