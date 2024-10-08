from django.db import models

class Peticion(models.Model):
    nombre = models.CharField(max_length=200)
    dia_reserva = models.DateField()
    num_personas = models.IntegerField()
    observaciones = models.CharField(max_length=200)

class Reserva(models.Model):
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ], default='pendiente')

    def __str__(self):
        return f"Reserva para {self.peticion.nombre} - Estado: {self.estado}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Peticion, on_delete=models.CASCADE)  # Relación con Peticion
    comida = models.CharField(max_length=200)  # Nombre del plato
    cantidad = models.IntegerField()  # Cantidad del plato
    observaciones = models.CharField(max_length=200, blank=True)  # Observaciones
    fecha_pedido = models.DateTimeField(auto_now_add=True)  # Fecha del pedido
    estado = models.CharField(max_length=10, choices=[
        ('pendiente', 'Pendiente'),
        ('preparado', 'Preparado'),
        ('recogido', 'Recogido'),
    ], default='pendiente')

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {self.comida} x{self.cantidad} ({self.estado})"
