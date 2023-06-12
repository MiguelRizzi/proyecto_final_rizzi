from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models, forms 

# * Tipo de Habitacion

class TipoHabitacionDetail(LoginRequiredMixin, DetailView):
    model = models.TipoHabitacion

class TipoHabitacionList(LoginRequiredMixin, ListView):
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

class TipoHabitacionDelete(LoginRequiredMixin, DeleteView):
    model = models.TipoHabitacion
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")

class TipoHabitacionUpdate(LoginRequiredMixin, UpdateView):
    model = models.TipoHabitacion
    success_url = reverse_lazy("hotel:index")
    form_class = forms.TipoHabitacionForm


# * Habitacion

class HabitacionDetail(LoginRequiredMixin, DetailView):
    model = models.Habitacion

class HabitacionList(LoginRequiredMixin, ListView):
    model = models.Habitacion
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Habitacion.objects.filter(numero__icontains=query)
        else:
            object_list = models.Habitacion.objects.all()
        return object_list

class HabitacionCreateView(LoginRequiredMixin, CreateView):
    model = models.Habitacion
    form_class = forms.HabitacionForm
    success_url = reverse_lazy("hotel:index")

class HabitacionDelete(LoginRequiredMixin, DeleteView):
    model = models.Habitacion
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")

class HabitacionUpdate(LoginRequiredMixin, UpdateView):
    model = models.Habitacion
    success_url = reverse_lazy("hotel:index")
    form_class = forms.HabitacionForm


# * Reserva

class ReservaDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Reserva
    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario es el cliente o si es personal del staff, False de lo contrario."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.is_staff

class ReservaList(LoginRequiredMixin, ListView):
    model = models.Reserva
    def get_queryset(self):
        """Si el usuario no es un miembro del staff, solo
        objetos que pertenecen al usuario que realiza la solicitud."""
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(cliente=self.request.user)
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            if self.request.user.is_staff:
                queryset = queryset.filter(cliente__username__icontains=query)
            else:
                queryset = queryset.filter(cliente=self.request.user, cliente__username__icontains=query)
        return queryset

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = models.Reserva
    form_class = forms.ReservaForm
    success_url = reverse_lazy("hotel:index")
    
    def form_valid(self, form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)

class ReservaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Reserva
    template_name = "hotel/confirm_delete.html"
    success_url = reverse_lazy("hotel:index")
    def test_func(self):
        """Determina el acceso a la vista, devuelve True si el usuario es el cliente o si es personal del staff, False de lo contrario."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.is_staff

class ReservaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Reserva
    success_url = reverse_lazy("hotel:index")

    form_class = forms.ReservaForm
    def test_func(self):
        """Determina el acceso a la vista, evuelve True si el usuario es el cliente o si es personal del staff, False de lo contrario."""
        reserva = self.get_object()
        return reserva.cliente == self.request.user or self.request.user.is_staff

