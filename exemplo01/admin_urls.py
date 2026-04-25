from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('procedimento/', views.pagina5, name='procedimento_list'),
    path('procedimento_executado/', views.pagina6, name='procedimento_executado_list'),
]