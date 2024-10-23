from django.urls import path
from reservas.views import PlatosListView, MisPedidosCreateView, MisPedidosListView, CrearPedidoView, CatalogoPlatosListView, BebidasListView,LogoutView, IniciarSesion, RegistroUsuario, CerrarSesion
from .views import HomeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('platos/', PlatosListView.as_view(), name='platos_list'),  
    path('catalogo_platos/', CatalogoPlatosListView.as_view(), name='catalogo_platos_list'),
    path('mispedidos/', MisPedidosListView.as_view(), name='mispedidos_list'),    
    path('bebidas/', BebidasListView.as_view(), name='bebidas_list'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crearpedido/', CrearPedidoView.as_view(), name='crearpedido_list'),    
    path('login/', IniciarSesion.as_view(), name='login'),
    path('register/', RegistroUsuario.as_view(), name='register'),  # Aquí corregido con ()
]


