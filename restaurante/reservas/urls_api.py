# reservas/urls_api.py
from django.urls import path
from .views import PlatoListCreateView, PlatoDetailView, BebidaListCreateView, BebidaDetailView

urlpatterns = [
    path('platosapi/', PlatoListCreateView.as_view(), name='plato-list-create'),  
    path('platosapi/<int:pk>/', PlatoDetailView.as_view(), name='plato-detail'),  
    path('bebidasapi/', BebidaListCreateView.as_view(), name='bebida-list-create'),  
    path('bebidasapi/<int:pk>/', BebidaDetailView.as_view(), name='bebida-detail'),  
]
