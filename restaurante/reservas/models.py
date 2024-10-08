from django.db import models

class Peticion(models.Model):
    nombre = models.CharField(max_length=200)
    dia_reserva = models.DateField()
    num_personas = models.IntegerField()
    observaciones = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Petición"
        verbose_name_plural = "Peticiones"

class Reserva(models.Model):
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=200)  # Nombre del cliente que hace el pedido
    comida = models.URLField()  # URL para seleccionar la comida
    estado = models.CharField(max_length=50, default='Pendiente')  # Estado del pedido
    fecha_pedido = models.DateField(auto_now_add=True)  # Fecha en que se realizó el pedido

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.estado}"

class EstadoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='estados')  # Relación con el pedido
    estado = models.CharField(max_length=50)  # Estado del pedido
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Fecha de la última actualización

    class Meta:
        verbose_name = "Estado de Pedido"
        verbose_name_plural = "Estados de Pedidos"

    def __str__(self):
        return f"Estado de {self.pedido.nombre_cliente}: {self.estado}"
