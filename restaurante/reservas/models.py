from django.db import models

class Peticion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()  # Para seleccionar el día con un calendario
    numero_personas = models.PositiveIntegerField(default=1)  # Con flechas para indicar cantidad
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Petición"  # Nombre en singular que aparecerá en el admin
        verbose_name_plural = "Peticiones"  # Nombre en plural que aparecerá en el admin

    def __str__(self):
        return f"{self.nombre} - {self.fecha} ({self.numero_personas} personas)"


class Reserva(models.Model):
    ESTADOS = [
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('pendiente', 'Pendiente'),
    ]

    peticion = models.OneToOneField(Peticion, on_delete=models.CASCADE)  # Relación uno a uno
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')

    class Meta:
        verbose_name = "Reserva"  # Nombre en singular que aparecerá en el admin
        verbose_name_plural = "Reservas"  # Nombre en plural que aparecerá en el admin

    def __str__(self):
        return f"Reserva para {self.peticion.nombre} - Estado: {self.estado}"
