from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nombre_per = models.CharField(max_length=50)

class Tipo_comida(models.Model):
    tipo_comida = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo comida"
        verbose_name_plural = "Tipos de comidas"

    def __str__(self):
        return self.tipo_comida

class Tipo_ingrediente(models.Model):
    tipo_ingrediente = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo ingrediente"
        verbose_name_plural = "Tipos de ingredientes"

    def __str__(self):
        return self.tipo_ingrediente

class Tipo_bebida(models.Model):
    tipo_bebida = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo bebida"
        verbose_name_plural = "Tipos de bebidas"

    def __str__(self):
        return self.tipo_bebida

class Bebidas(models.Model):
    nom_bebida = models.CharField(max_length=100)
    precio_bebida = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tipo_bebi = models.ManyToManyField(Tipo_bebida, related_name='bebidas', blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

    def __str__(self):
        return self.nom_bebida

class Ingrediente(models.Model):
    tipo = models.ForeignKey(Tipo_ingrediente, related_name='ingredientes', on_delete=models.CASCADE, default=1)  # Cambiado el related_name
    nombre_ingrediente = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.nombre_ingrediente

class Platos(models.Model):
    nombre_plato = models.CharField(max_length=100)
    precio_plato = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_comida = models.ForeignKey(Tipo_comida, on_delete=models.CASCADE, default=1)  # Asume que el tipo de comida con ID 1 es el valor predeterminado
    ingredientes = models.ManyToManyField(Ingrediente)
    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"

    def __str__(self):
        return self.nombre_plato

class EstadoPedido(models.Model):
    estado = models.CharField(max_length=20)

class MisPedidos(models.Model):
    nombre_persona = models.CharField(max_length=50)
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)  # Relaciona el pedido directamente con un plato
    cantidad = models.PositiveIntegerField(default=1)
    observaciones = models.TextField(blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)  # Registra automáticamente la fecha del pedido

    class Meta:
        verbose_name = "Pedido para recoger"
        verbose_name_plural = "Pedidos para recoger"

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre_plato} (Pedido de {self.nombre_persona})"

    def total_precio(self):
        return self.plato.precio_plato * self.cantidad

class CatalogoPlatos(models.Model):
    ESTRELLAS = [
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE, related_name='catalogo_platos')
    valoracion = models.IntegerField(choices=ESTRELLAS, default=0)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Catálogo de Plato"
        verbose_name_plural = "Catálogo de Platos"

    def __str__(self):
        return f"{self.plato.nombre_plato} - {self.valoracion} estrellas"

    @property
    def precio_plato(self):
        return self.plato.precio_plato
