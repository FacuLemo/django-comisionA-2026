from django.urls import path

from . import views

urlpatterns = [
    path("", views.saludos, name="hola"),
    path("adios/", views.despedir, name="adios")
]
