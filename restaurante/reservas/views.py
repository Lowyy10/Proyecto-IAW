from reservas.models import Platos, CatalogoPlatos, Bebidas, MisPedidos
from django.views.generic import FormView,ListView, TemplateView, FormView, ListView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,MisPedidosForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView

# Vistas para mostrar listas de objetos
class MisPedidosCreateView(CreateView):
    model = MisPedidos
    form_class = MisPedidosForm
    template_name = 'reservas/mispedidos_list.html'  # El template donde se muestra el formulario
    success_url = reverse_lazy('mispedidos_list')  # Redirigir a la lista de pedidos tras el éxito

    def form_valid(self, form):
        # Aquí puedes agregar lógica adicional si es necesario
        return super().form_valid(form)
    
class CrearPedidoView(CreateView):
    model = MisPedidos
    form_class = MisPedidosForm
    template_name = 'reservas/crearpedido_list.html'
    success_url = reverse_lazy('mispedidos_list')  # Redirige a la vista de pedidos después de crear el pedido

    def form_valid(self, form):
        # Puedes realizar cualquier acción adicional aquí antes de guardar el formulario
        return super().form_valid(form)

class PlatosListView(ListView):
    model = Platos

class BebidasListView(ListView):
    model = Bebidas
    context_object_name = 'photos'

class CatalogoPlatosListView(ListView):
    model = CatalogoPlatos

class MisPedidosListView(LoginRequiredMixin, ListView):
    model = MisPedidos
    login_url = 'login'
    def get_queryset(self):
        # Puedes filtrar los pedidos según el usuario o cualquier otro criterio
        return MisPedidos.objects.all()


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
