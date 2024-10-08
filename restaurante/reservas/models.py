from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    estado = models.CharField(max_length=50, default='Pendiente')  # Estado predeterminado

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva a nombre de {self.peticion.nombre} para el {self.peticion.dia_reserva}"

    # Métodos para obtener los datos de Peticion
    @property
    def dia_reserva(self):
        return self.peticion.dia_reserva

    @property
    def num_personas(self):
        return self.peticion.num_personas

    @property
    def observaciones(self):
        return self.peticion.observaciones

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=200)  # Nombre del cliente que hace el pedido
    comida = models.CharField(max_length=200)  
    fecha_pedido = models.DateField(auto_now_add=True)  # Fecha en que se realizó el pedido

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido de {self.nombre_cliente}"

class EstadoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='estados')  # Relación con el pedido
    estado = models.CharField(max_length=50)  # Estado del pedido
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Fecha de la última actualización

    class Meta:
        verbose_name = "Estado de Pedido"
        verbose_name_plural = "Estados de Pedidos"

    def __str__(self):
        return f"Estado de {self.pedido.nombre_cliente}: {self.estado}"

@receiver(post_save, sender=Pedido)
def crear_estado_pedido(sender, instance, created, **kwargs):
    if created:  # Solo se ejecuta si el pedido ha sido creado
        EstadoPedido.objects.create(pedido=instance, estado='Pendiente')  # Crea un nuevo estado

