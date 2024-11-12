# reservas/urls_api.py
from django.urls import path
from .views import PlatoListCreateView, PlatoDetailView, BebidaListCreateView, BebidaDetailView

urlpatterns = [
    path('platos/', PlatoListCreateView.as_view(), name='plato-list-create'),  
    path('platos/<int:pk>/', PlatoDetailView.as_view(), name='plato-detail'),  
    path('bebidas/', BebidaListCreateView.as_view(), name='bebida-list-create'),  
    path('bebidas/<int:pk>/', BebidaDetailView.as_view(), name='bebida-detail'),  
]
