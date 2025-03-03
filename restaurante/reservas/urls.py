# reservas/urls.py
from django.urls import path, include
from .views import (
    PlatosListView, MisPedidosListView, BebidasListView, HomeView,
    PedidoDeleteView, CrearPedidoView, IniciarSesion, RegistroUsuario,
    editar_perfil, eliminar_perfil, ver_perfil, ValoracionEliminarPlatoView, ValoracionEliminarBebidaView
)
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('platos/', PlatosListView.as_view(), name='platos_list'),  
    path('mispedidos/', MisPedidosListView.as_view(), name='mispedidos_list'),    
    path('bebidas/', BebidasListView.as_view(), name='bebidas_list'),
    path('', HomeView.as_view(), name='home'),
    path('mispedidos/eliminar/<int:pk>/', PedidoDeleteView.as_view(), name='pedido_eliminar'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crear_pedido/', CrearPedidoView.as_view(), name='crearpedido_list'),    
    path('login/', IniciarSesion.as_view(), name='login'),
    path('register/', RegistroUsuario.as_view(), name='register'),
    path('registration/editar_perfil/', editar_perfil, name='editar_perfil'),
    path('registration/eliminar_perfil/', eliminar_perfil, name='eliminar_perfil'), 
    path('registration/ver_perfil.html', ver_perfil, name='perfil'),
   # path('valoracion/eliminar/<int:valoracion_id>/', ValoracionEliminarView.as_view(), name='valoracion_eliminar'),
    path('eliminar/valoracion/plato/<int:valoracion_id>/', ValoracionEliminarPlatoView.as_view(), name='eliminar_valoracion_plato'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('eliminar/valoracion/bebida/<int:valoracion_id>/', ValoracionEliminarBebidaView.as_view(), name='eliminar_valoracion_bebida'),
    # API URLs
    path('api/', include('reservas.urls_api')),  # Agrega las rutas de la API bajo el prefijo /api/
]
