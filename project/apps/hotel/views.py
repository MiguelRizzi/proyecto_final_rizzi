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
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")

class TipoHabitacionUpdate(UpdateView):
    model = models.TipoHabitacion
    success_url = reverse_lazy("hotel:index")
    form_class = forms.TipoHabitacionForm


# * Habitacion

class HabitacionDetail(DetailView):
    model = models.Habitacion

class HabitacionList(ListView):
    model = models.Habitacion

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Habitacion.objects.filter(numero = query)
        else:
            object_list = models.Habitacion.objects.all()
        return object_list

class HabitacionCreateView(LoginRequiredMixin, CreateView):
    model = models.Habitacion
    form_class = forms.HabitacionForm
    success_url = reverse_lazy("hotel:index")

class HabitacionDelete(DeleteView):
    model = models.Habitacion
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")

class HabitacionUpdate(UpdateView):
    model = models.Habitacion
    success_url = reverse_lazy("hotel:index")
    form_class = forms.HabitacionForm


# * Reserva

class ReservaDetail(DetailView):
    model = models.Reserva

class ReservaList(ListView):
    model = models.Reserva

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Reserva.objects.filter(cliente__icontains = query)
        else:
            object_list = models.Reserva.objects.all()
        return object_list

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = models.Reserva
    form_class = forms.ReservaForm
    success_url = reverse_lazy("hotel:index")
    
    def form_valid(self, form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)

class ReservaDelete(DeleteView):
    model = models.Reserva
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")

class ReservaUpdate(UpdateView):
    model = models.Reserva
    success_url = reverse_lazy("hotel:index")
    form_class = forms.ReservaForm
