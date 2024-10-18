from reservas.models import Platos, CatalogoPlatos, Pedidos, Bebidas
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse

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