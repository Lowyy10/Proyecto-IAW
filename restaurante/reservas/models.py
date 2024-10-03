from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    numero_personas = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario} para {self.numero_personas} personas el {self.fecha_reserva} a las {self.hora_reserva}'
