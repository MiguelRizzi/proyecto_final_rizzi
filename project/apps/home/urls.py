from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/index.html"), name="index"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("perfil/detail/<int:pk>", views.PerfilDetail.as_view(), name="perfil_detail"),
    path("perfil/create/", views.PerfilCreate.as_view(), name="perfil_create"),
    path("perfil/update/<int:pk>", views.PerfilUpdate.as_view(), name="perfil_update"),
    path("perfil/delete/<int:pk>", views.PerfilDelete.as_view(), name="perfil_delete"),

]

urlpatterns += staticfiles_urlpatterns()
