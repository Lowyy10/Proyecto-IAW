# filters.py
from django_filters import rest_framework as filters
from .models import Bebidas,Platos
from django.db import models

class BebidaFilter(filters.FilterSet):
    class Meta:
        model = Bebidas
        fields = '__all__'  # Permite filtrar por cualquier campo del modelo

        # Ignora el campo ImageField estableciendo una anulación
        filter_overrides = {
            models.ImageField: {
                'filter_class': filters.CharFilter  # Usa un filtro de texto para ignorar las imágenes
            }
        }


class PlatoFilter(filters.FilterSet):
    class Meta:
        model = Platos
        fields = '__all__'  # Permite filtrar por cualquier campo del modelo

        # Si algún campo es de tipo ImageField, se ignora o se le asigna un filtro adecuado
        filter_overrides = {
            models.ImageField: {
                'filter_class': filters.CharFilter  # Usa un filtro de texto para ignorar las imágenes
            }
        }