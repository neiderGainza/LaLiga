from django.urls import path
from . import views

name = "teams"
urlpatterns = [
    path('', views.prueba, name = "prueba"),
]
