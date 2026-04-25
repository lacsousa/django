from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listamedico/', views.listamedico, name='listamedico'),
    path('listaPaciente/', views.listaPaciente, name='listaPaciente'),
    path('detalheConsulta/', views.detalheConsulta, name='detalheConsulta'),
    path('novaConsulta/', views.novaConsulta, name='novaConsulta'),
]