from django.urls import path
from . import views

name = "tournaments"
urlpatterns = [
    path('', views.prueba, name = "prueba"),
]
