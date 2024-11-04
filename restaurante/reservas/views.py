from reservas.models import Platos, Bebidas, MisPedidos, Perfil,Valoracion
from django.views.generic import FormView,View,ListView, TemplateView, FormView, ListView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm,MisPedidosForm,PerfilForm,ValoracionForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.db import models
from django.contrib.auth.decorators import login_required


# Vistas para mostrar listas de objetos

class MisPedidosCreateView(CreateView):
    model = MisPedidos
    form_class = MisPedidosForm
    template_name = 'reservas/mispedidos_list.html'  # El template donde se muestra el formulario
    success_url = reverse_lazy('mispedidos_list')  # Redirigir a la lista de pedidos tras el éxito

    def form_valid(self, form):
        # Aquí puedes agregar lógica adicional si es necesario
        return super().form_valid(form)

class PedidoDeleteView(DeleteView):
    model = MisPedidos
    success_url = reverse_lazy("mispedidos_list")

class CrearPedidoView(CreateView):
    model = MisPedidos
    form_class = MisPedidosForm
    template_name = 'reservas/crearpedido_list.html'
    success_url = reverse_lazy('mispedidos_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual al pedido
        return super().form_valid(form)

class PlatosListView(ListView):
    model = Platos

class ValoracionEliminarView(View):
    def post(self, request, *args, **kwargs):
        valoracion_id = kwargs.get('valoracion_id')
        # Obtén la valoración, asegurándote de que pertenezca al usuario actual
        valoracion = get_object_or_404(Valoracion, id=valoracion_id, usuario=request.user)
        valoracion.delete()  # Elimina la valoración
        return redirect('bebidas_list')
    
class BebidasListView(ListView):
    model = Bebidas
    context_object_name = 'photos'
    template_name = 'tu_template_de_bebidas.html'  # Asegúrate de especificar el nombre correcto de tu plantilla

    def post(self, request, *args, **kwargs):
        bebida_id = request.POST.get('bebida_id')
        bebida = get_object_or_404(Bebidas, id=bebida_id)
        valoracion_form = ValoracionForm(request.POST)

        if valoracion_form.is_valid():
            Valoracion.objects.update_or_create(
                bebida=bebida,
                usuario=request.user,
                defaults={'valoracion': valoracion_form.cleaned_data['valoracion']}
            )
            return redirect('bebidas_list')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valoracion_form'] = ValoracionForm()
        for bebida in context['photos']:
            # Calcular la media de las valoraciones
            valoraciones = bebida.valoraciones.all()
            if valoraciones.exists():
                media_valoracion = valoraciones.aggregate(models.Avg('valoracion'))['valoracion__avg']
                bebida.media_valoracion = round(media_valoracion, 2)  # Redondear a dos decimales
            else:
                bebida.media_valoracion = 0  # Sin valoraciones, media es 0
        return context



class MisPedidosListView(ListView):
    model = MisPedidos
    template_name = 'reservas/mispedidos_list.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        # Filtra los pedidos para mostrar solo los del usuario autenticado
        return MisPedidos.objects.filter(usuario=self.request.user)


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

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a una página que muestre el perfil actualizado
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'registration/editar_perfil.html', {'form': form})

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'registration/ver_perfil.html', {'perfil': perfil})
