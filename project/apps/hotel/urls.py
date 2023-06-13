from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("", TemplateView.as_view(template_name="hotel/index.html"), name="index"),
    # Tipo de habitacion
    path("tipohabitacion/detail/<int:pk>", staff_member_required(views.TipoHabitacionDetail.as_view()), name="tipohabitacion_detail"),
    path("tipohabitacion/list/", staff_member_required(views.TipoHabitacionList.as_view()), name="tipohabitacion_list"),
    path("tipohabitacion/create/", staff_member_required(views.TipoHabitacionCreateView.as_view()), name="tipohabitacion_create"),
    path("tipohabitacion/delete/<int:pk>", staff_member_required(views.TipoHabitacionDelete.as_view()), name="tipohabitacion_delete"),
    path("tipohabitacion/update/<int:pk>", staff_member_required(views.TipoHabitacionUpdate.as_view()), name="tipohabitacion_update"),
    # Habitacion
    path("habitacion/detail/<int:pk>", views.HabitacionDetail.as_view(), name="habitacion_detail"),
    path("habitacion/list/", views.HabitacionList.as_view(), name="habitacion_list"),
    path("habitacion/create/", staff_member_required(views.HabitacionCreateView.as_view()), name="habitacion_create"),
    path("habitacion/delete/<int:pk>", staff_member_required(views.HabitacionDelete.as_view()), name="habitacion_delete"),
    path("habitacion/update/<int:pk>", staff_member_required(views.HabitacionUpdate.as_view()), name="habitacion_update"),
    # Reserva
    path("reserva/detail/<int:pk>", views.ReservaDetail.as_view(), name="reserva_detail"),
    path("reserva/list/", views.ReservaList.as_view(), name="reserva_list"),
    path("reserva/create/", views.ReservaCreateView.as_view(), name="reserva_create"),
    path("reserva/delete/<int:pk>", views.ReservaDelete.as_view(), name="reserva_delete"),
    path("reserva/update/<int:pk>", views.ReservaUpdate.as_view(), name="reserva_update"),
]

