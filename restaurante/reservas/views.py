from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reserva  # Importa el modelo de reservas si lo estás usando

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)  # Filtrar por usuario
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})
