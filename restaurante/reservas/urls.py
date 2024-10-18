from django.urls import path
from reservas.views import PlatosListView, PedidosListView, CatalogoPlatosListView, BebidasListView
from .views import HomeView

urlpatterns = [
    path('platos/', PlatosListView.as_view(), name='platos_list'),  # Verifica que el nombre sea 'platos_list'
    path('catalogo_platos/', CatalogoPlatosListView.as_view(), name='catalogo_platos_list'),
    path('pedidos/', PedidosListView.as_view(), name='pedidos_list'),
    path('bebidas/', BebidasListView.as_view(), name='bebidas_list'),
    path('', HomeView.as_view(), name='home'),
]

