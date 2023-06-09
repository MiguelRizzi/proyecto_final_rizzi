from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("", TemplateView.as_view(template_name="hotel/index.html"), name="index"),
    # Tipo de habitacion
    path("tipohabitacion/detail/<int:pk>", views.TipoHabitacionDetail.as_view(), name="tipohabitacion_detail"),
    path("tipohabitacion/list/", views.TipoHabitacionList.as_view(template_name="hotel/tipohabitacion_list.html"), name="tipohabitacion_list"),
    path("tipohabitacion/create/", staff_member_required(views.TipoHabitacionCreateView.as_view()), name="tipohabitacion_create"),
    path("tipohabitacion/delete/<int:pk>", staff_member_required(views.TipoHabitacionDelete.as_view()), name="tipohabitacion_delete"),
    path("tipohabitacion/update/<int:pk>", staff_member_required(views.TipoHabitacionUpdate.as_view()), name="tipohabitacion_update"),

    path("habitacion/create/", staff_member_required(views.HabitacionCreateView.as_view()), name="habitacion_create"),
    path("reserva/create/", staff_member_required(views.ReservaCreateView.as_view()), name="reserva_create"),
]

