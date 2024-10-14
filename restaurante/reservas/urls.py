from django.urls import path
from reservas.views import PlatosListView, PedidosListView, CatalogoPaltosListView
from .views import vista

urlpatterns = [

    path('platos/',PlatosListView.as_view()),
    path('catalogo_platos/',CatalogoPaltosListView.as_view()),
    path('pedidos/',PedidosListView.as_view()),
    path('',vista,name='vista')
] 