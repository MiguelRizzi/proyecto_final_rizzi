from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("", TemplateView.as_view(template_name="hotel/index.html"), name="index"),
    path("tipohabitacion/create/", staff_member_required(views.TipoHabitacionCreateView.as_view()), name="tipohabitacion_create"),
    path("habitacion/create/", staff_member_required(views.HabitacionCreateView.as_view()), name="habitacion_create"),
    path("reserva/create/", staff_member_required(views.ReservaCreateView.as_view()), name="reserva_create"),
    
]

