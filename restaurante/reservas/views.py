from reservas.models import Platos, Bebidas,ValoracionPlato, MisPedidos, Perfil,Valoracion, Tipo_bebida,Tipo_comida,Ingrediente
from django.views.generic import FormView,View,ListView, TemplateView, FormView, ListView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm,MisPedidosForm,PerfilForm,ValoracionForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.http import HttpResponseForbidden
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
    template_name = 'reservas/deletepedido_list.html'  # Asegúrate de que este sea el nombre correcto de tu plantilla
    success_url = reverse_lazy('mispedidos_list')  # Redirige a la lista de pedidos después de eliminar

    def get_object(self):
        # Obtener el pedido por su ID
        pedido = get_object_or_404(MisPedidos, pk=self.kwargs['pk'])

        # Verificar que el usuario autenticado sea el propietario del pedido
        if pedido.usuario != self.request.user:
            # Si el usuario no es el propietario, denegar el acceso
            messages.error(self.request, "No tienes permiso para eliminar ese pedido.")  # Mostrar mensaje de error
            return None  # Devolver None para que no se renderice el formulario de eliminación

        return pedido

    def get(self, request, *args, **kwargs):
        # Si no tienes permisos, redirigir inmediatamente
        pedido = self.get_object()
        if not pedido:
            return redirect('mispedidos_list')  # Redirige a la lista de pedidos si no tienes permiso
        
        # Si tienes permiso, proceder con la eliminación
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Aquí se maneja el formulario POST para eliminar el objeto
        pedido = self.get_object()
        if not pedido:
            return redirect('mispedidos_list')  # Si no tienes permiso, redirige a la lista de pedidos
        
        # Eliminar el objeto
        pedido.delete()
        
        # Redirigir a la lista de pedidos después de la eliminación
        messages.success(self.request, "Pedido eliminado con éxito.")
        return redirect(self.success_url)


class CrearPedidoView(CreateView):
    model = MisPedidos
    form_class = MisPedidosForm
    template_name = 'reservas/crearpedido_list.html'
    success_url = reverse_lazy('mispedidos_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual al pedido
        return super().form_valid(form)


from django.db.models import Q  # Importa Q para usar consultas más complejas

class PlatosListView(ListView):
    model = Platos
    context_object_name = 'object_list'
    template_name = 'platos_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valoracion_form'] = ValoracionForm()
        context['tipos_comida'] = Tipo_comida.objects.all()
        context['ingredientes'] = Ingrediente.objects.all()

        for plato in context['object_list']:
            valoraciones = plato.valoraciones.all()
            if valoraciones.exists():
                media_valoracion = valoraciones.aggregate(Avg('valoracion'))['valoracion__avg']
                plato.media_valoracion = round(media_valoracion, 2)
            else:
                plato.media_valoracion = 0

        return context

    def post(self, request, *args, **kwargs):
        plato_id = request.POST.get('plato_id')
        plato = get_object_or_404(Platos, id=plato_id)
        valoracion_form = ValoracionForm(request.POST)

        if valoracion_form.is_valid():
            ValoracionPlato.objects.update_or_create(
                plato=plato,
                usuario=request.user,
                defaults={'valoracion': valoracion_form.cleaned_data['valoracion']}
            )
            return redirect('platos_list')  # Cambia a la URL correcta para tu lista de platos

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get('nombre', '')
        tipo_id = self.request.GET.get('tipo', None)
        precio_maximo = self.request.GET.get('precio', None)
        ingrediente_id = self.request.GET.get('ingrediente', None)

        if nombre:
            queryset = queryset.filter(nombre_plato__icontains=nombre)
        if tipo_id:
            queryset = queryset.filter(tipo_comida__id=tipo_id)
        if precio_maximo:
            try:
                precio_maximo = float(precio_maximo)
                queryset = queryset.filter(precio_plato__lte=precio_maximo)
            except ValueError:
                pass
        if ingrediente_id:
            queryset = queryset.filter(ingredientes__id=ingrediente_id)

        return queryset

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
    template_name = 'bebidas_list'  # Asegúrate de especificar el nombre correcto de tu plantilla

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

        # Calcular la media de las valoraciones para cada bebida
        for bebida in context['photos']:
            valoraciones = bebida.valoraciones.all()
            if valoraciones.exists():
                media_valoracion = valoraciones.aggregate(models.Avg('valoracion'))['valoracion__avg']
                bebida.media_valoracion = round(media_valoracion, 2)  # Redondear a dos decimales
            else:
                bebida.media_valoracion = 0  # Sin valoraciones, media es 0
        
        # Obtener los tipos de bebida para el filtro
        context['tipos_bebida'] = Tipo_bebida.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de búsqueda
        nombre = self.request.GET.get('nombre', '')
        tipo_id = self.request.GET.get('tipo', None)
        precio_maximo = self.request.GET.get('precio', None)

        # Filtrar por nombre
        if nombre:
            queryset = queryset.filter(nom_bebida__icontains=nombre)

        # Filtrar por tipo
        if tipo_id:
            queryset = queryset.filter(tipo_bebi__id=tipo_id)

        # Filtrar por precio
        if precio_maximo:
            queryset = queryset.filter(precio_bebida__lte=precio_maximo)

        return queryset


class MisPedidosListView(ListView):
    model = MisPedidos
    template_name = 'reservas/mispedidos_list.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        # Filtra los pedidos para mostrar solo los del usuario autenticado
        return MisPedidos.objects.filter(usuario=self.request.user)


from django.db.models import Avg
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener los 3 platos más valorados
        context['top_platos'] = Platos.objects.annotate(
            media_valoracion=Avg('valoraciones__valoracion')
        ).order_by('-media_valoracion')[:3]  # Solo los 3 primeros
        return context


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
    success_url = reverse_lazy('home')  # Redirige al login tras el registro exitoso

    def form_valid(self, form):
        user = form.save()  # Guarda el nuevo usuario
        login(self.request, user)  # Inicia sesión automáticamente después del registro (opcional)
        return super().form_valid(form)
    
@login_required
def eliminar_perfil(request):
    # Obtén el perfil del usuario que ha iniciado sesión
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == 'POST':
        # Primero, eliminamos el perfil
        perfil.delete()
        # Luego, eliminamos el usuario
        request.user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        return redirect('home')  # Redirige a la página de inicio o a donde desees

    return render(request, 'eliminar_perfil.html', {'perfil': perfil})

# Vista para cerrar sesión
class CerrarSesion(LogoutView):
    next_page = 'home'  # Redirige a la página de inicio tras cerrar sesión

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)  # Obtiene el perfil del usuario autenticado
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('home')  # O redirige a donde desees
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'registration/editar_perfil.html', {'form': form})

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'registration/ver_perfil.html', {'perfil': perfil})

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PlatoSerializer, BebidaSerializer
from .filters import BebidaFilter, PlatoFilter
from django_filters import rest_framework as filters

class PlatoListCreateView(generics.ListCreateAPIView):
    queryset = Platos.objects.all()
    serializer_class = PlatoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PlatoFilter

class PlatoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platos.objects.all()
    serializer_class = PlatoSerializer

class BebidaListCreateView(generics.ListCreateAPIView):
    queryset = Bebidas.objects.all()
    serializer_class = BebidaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BebidaFilter

class BebidaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bebidas.objects.all()
    serializer_class = BebidaSerializer