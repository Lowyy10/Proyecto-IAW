from reservas.models import Platos, CatalogoPlatos
from django.views.generic import ListView


class PlatosListView(ListView):
    model = Platos

class CatalogoPaltosListView(ListView):
    model = CatalogoPlatos

    