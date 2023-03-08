from django.urls import path
from . import views

name = "players"
urlpatterns = [
    path('', views.prueba, name = "prueba"),
]
