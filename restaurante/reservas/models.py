from django.db import models

class Platos(models.Model):
    nombre_plato = models.CharField(max_length=100)
    precio_plato = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"

    def __str__(self):
        return self.nombre_plato


class Pedidos(models.Model):
    nombre_persona = models.CharField(max_length=50)
    platos = models.ManyToManyField(Platos, through='PedidoPlato', related_name='pedidos')  # Relación con Platos

    class Meta:
        verbose_name = "Pedido para recoger"
        verbose_name_plural = "Pedidos para recoger"

    def __str__(self):
        return f"Pedido de {self.nombre_persona}"

    def total_precio(self):
        return sum(pedido_plato.plato.precio_plato * pedido_plato.cantidad for pedido_plato in self.pedido_platos.all())


class PedidoPlato(models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    observaciones = models.TextField(blank=True, null=True)
    pedido = models.ForeignKey(Pedidos, related_name='pedido_platos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Plato en Pedido"
        verbose_name_plural = "Platos en Pedido"

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre_plato}"


class CatalogoPlatos(models.Model):
    ESTRELLAS = [
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    nombre_plato = models.ForeignKey(Platos, on_delete=models.CASCADE, related_name='catalogo_platos')
    valoracion = models.IntegerField(choices=ESTRELLAS, default=0)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Catálogo de Plato"
        verbose_name_plural = "Catálogo de Platos"

    def __str__(self):
        return f"{self.nombre_plato.nombre_plato} - {self.valoracion} estrellas"

    @property
    def precio_plato(self):
        return self.nombre_plato.precio_plato  # Obtener el precio del plato relacionado