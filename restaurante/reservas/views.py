from reservas.models import Platos, CatalogoPlatos, Pedidos, Bebidas
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Bebidas, Tipo_bebida
from django.contrib import messages

class PlatosListView(ListView):
    model = Platos

class BebidasListView(ListView):
    model = Bebidas
    context_object_name = 'photos'

class CatalogoPlatosListView(ListView):
    model = CatalogoPlatos

class PedidosListView(ListView):
    model = Pedidos

class HomeView(TemplateView):
    template_name = 'home.html'

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout

@login_required
def confirm_logout(request):
    if request.method == 'POST':
        logout(request)  # Cierra la sesión
        return redirect('home')  # Redirige a la página de inicio
    return render(request, 'confirm_logout.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            messages.success(request, f'Bienvenido {user.username}, has sido registrado con éxito.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, f'Bienvenido de nuevo, {form.get_user().username}.')
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})