from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.login, name="login"),
    path("registrations",views.registration,name="registrations")
]