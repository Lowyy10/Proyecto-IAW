from django.urls import path
from . import views

urlpatterns = [
    # Asegúrate de tener al menos una URL definida, por ejemplo:
    path('', views.lista_reservas, name='reservas_list'),
]