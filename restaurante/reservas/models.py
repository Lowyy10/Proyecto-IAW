from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.email}"
    

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
    ESTRELLAS = [
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    valoracion = models.IntegerField(choices=ESTRELLAS, default=0)
    nom_bebida = models.CharField(max_length=100)
    precio_bebida = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tipo_bebi = models.ManyToManyField(Tipo_bebida, related_name='bebidas', blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

    def __str__(self):
        return self.nom_bebida



class Valoracion(models.Model):
    bebida = models.ForeignKey(Bebidas, on_delete=models.CASCADE, related_name='valoraciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField(choices=Bebidas.ESTRELLAS)

    class Meta:
        unique_together = ('bebida', 'usuario')  # Evitar que un usuario valore la misma bebida más de una vez

    def __str__(self):
        return f"{self.usuario.username} - {self.bebida.nom_bebida} - {self.valoracion} estrellas"

class Ingrediente(models.Model):
    tipo = models.ForeignKey(Tipo_ingrediente, related_name='ingredientes', on_delete=models.CASCADE, default=1)  # Relacionar ingrediente con tipo
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
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)  # Los ingredientes están ahora relacionados con los tipos
    image = models.ImageField(upload_to='photos/', blank=True)

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"

    def __str__(self):
        return self.nombre_plato

class ValoracionPlato(models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE, related_name='valoraciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField(choices=Bebidas.ESTRELLAS)

    class Meta:
        unique_together = ('plato', 'usuario')  # Evitar valoraciones duplicadas por usuario

    def __str__(self):
        return f"{self.usuario.username} - {self.plato.nombre_plato} - {self.valoracion} estrellas"


class EstadoPedido(models.Model):
    estado = models.CharField(max_length=20)

class MisPedidos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Sin valor por defecto
    nombre_persona = models.CharField(max_length=50)
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)  # Asegúrate de que existan platos en la base de datos
    cantidad = models.PositiveIntegerField(default=1)
    observaciones = models.TextField(blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pedido para recoger"
        verbose_name_plural = "Pedidos para recoger"

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre_plato} (Pedido de {self.nombre_persona})"

    def total_precio(self):
        return self.plato.precio_plato * self.cantidad

    @property
    def precio_plato(self):
        return self.plato.precio_plato
