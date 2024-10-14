from reservas.models import Platos, CatalogoPlatos, Pedidos
from django.views.generic import ListView
from django.http import HttpResponse


class PlatosListView(ListView):
    model = Platos

class CatalogoPaltosListView(ListView):
    model = CatalogoPlatos

class PedidosListView(ListView):
    model = Pedidos

def vista(request):
    return HttpResponse('Esta es mi primera vista')
    