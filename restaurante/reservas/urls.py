from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='register'),
    # Otras URLs como las de reservas
]