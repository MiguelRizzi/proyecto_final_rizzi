from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/index.html"), name="index"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()
