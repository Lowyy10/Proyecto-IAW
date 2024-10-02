from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reservas_list')  # Redirigir a la lista de reservas
    else:
        form = RegistroForm()
    return render(request, 'reservas/registro.html', {'form': form})