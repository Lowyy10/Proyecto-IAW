from reservas.models import Platos, CatalogoPlatos, Pedidos, Bebidas,PedidoPlato
from django.views.generic import FormView,ListView, TemplateView, FormView, ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PedidoForm,CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Vistas para mostrar listas de objetos
class CrearPedidoView(CreateView):
    model = PedidoPlato
    fields = ["plato", "cantidad", "observaciones"]  #esto hay que importarlo

class PlatosListView(ListView):
    model = Platos

class BebidasListView(ListView):
    model = Bebidas
    context_object_name = 'photos'

class CatalogoPlatosListView(ListView):
    model = CatalogoPlatos

class PedidosListView(LoginRequiredMixin, ListView):
    model = Pedidos
    login_url = 'login'
    redirect_field_name = 'pedidos'

class HomeView(TemplateView):
    template_name = 'home.html'

# Vista para iniciar sesión
class IniciarSesion(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  # Redirige a la página de inicio tras iniciar sesión correctamente

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

# Vista para registrarse
class RegistroUsuario(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm  # Usa tu formulario personalizado o el de Django
    success_url = reverse_lazy('login')  # Redirige al login tras el registro exitoso

    def form_valid(self, form):
        user = form.save()  # Guarda el nuevo usuario
        login(self.request, user)  # Inicia sesión automáticamente después del registro (opcional)
        return super().form_valid(form)

# Vista para cerrar sesión
class CerrarSesion(LogoutView):
    next_page = 'home'  # Redirige a la página de inicio tras cerrar sesión
