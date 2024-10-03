from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario} el {self.fecha} a las {self.hora}'
