from django.contrib import admin
from .models import Peticion, Reserva, Pedido, EstadoPedido
@admin.register(Peticion)
class PeticionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dia_reserva', 'num_personas', 'observaciones')
    search_fields = ('nombre', 'observaciones')
    list_filter = ('dia_reserva', 'num_personas')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona', 'dia_reserva', 'num_personas', 'estado', 'observaciones')
    search_fields = ('peticion__nombre',)
    list_filter = ('peticion__dia_reserva', 'estado')

    def nombre_persona(self, obj):
        return obj.peticion.nombre
    
    def dia_reserva(self, obj):
        return obj.peticion.dia_reserva
    
    def num_personas(self, obj):
        return obj.peticion.num_personas

    def observaciones(self, obj):
        return obj.peticion.observaciones

    def estado(self, obj):
        return obj.estado
    
    estado.short_description = 'Estado de la Reserva'
    nombre_persona.short_description = 'Nombre de la Persona'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'comida', 'estado', 'fecha_pedido')
    search_fields = ('nombre_cliente',)  # Busca por el nombre del cliente
    list_filter = ('estado', 'fecha_pedido')  # Filtrar por estado y fecha

@admin.register(EstadoPedido)
class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'estado', 'fecha_actualizacion')
    search_fields = ('pedido__nombre_cliente', 'estado')  # Busca por el nombre del cliente del pedido
    list_filter = ('estado',)  # Filtrar por estado
