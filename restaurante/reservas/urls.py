from django.urls import path
from reservas.views import PlatosListView, CatalogoPaltosListView

urlpatterns = [
    path('platos/',PlatosListView.as_view()),
    path('catalogo_platos/',CatalogoPaltosListView.as_view())

] 