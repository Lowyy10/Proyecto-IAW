from django.urls import path
from .views import ReservaCreateView

app_name = 'reservas'

urlpatterns = [
    path('nueva/', ReservaCreateView.as_view(), name='crear_reserva'),  # Ruta para crear una nueva reserva
]
