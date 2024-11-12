# serializers.py
from rest_framework import serializers
from .models import Platos, Bebidas

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = '__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebidas
        fields = '__all__'
