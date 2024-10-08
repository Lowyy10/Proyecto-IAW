from django.contrib import admin
from .models import Peticion, Reserva, Pedido

@admin.register(Peticion)
class PeticionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dia_reserva', 'num_personas', 'observaciones')
    search_fields = ('nombre', 'observaciones')
    list_filter = ('dia_reserva', 'num_personas')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona', 'dia_reserva', 'num_personas', 'estado', 'observaciones')
    search_fields = ('peticion__nombre',)  # Busca por el nombre en Peticion
    list_filter = ('peticion__dia_reserva', 'estado')  # Filtrar por estado y fecha

    # Campos calculados en la lista de visualización
    def nombre_persona(self, obj):
        return obj.peticion.nombre  # Devuelve el nombre de la persona de la petición
    
    def dia_reserva(self, obj):
        return obj.dia_reserva
    
    def num_personas(self, obj):
        return obj.num_personas

    def observaciones(self, obj):
        return obj.observaciones

    # Mostrar el estado directamente en el admin
    def estado(self, obj):
        return obj.estado
    
    estado.short_description = 'Estado de la Reserva'  # Encabezado personalizado
    nombre_persona.short_description = 'Nombre de la Persona'  # Encabezado personalizado

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'comida', 'cantidad', 'estado', 'fecha_pedido')
    search_fields = ('cliente__nombre', 'comida')  # Permite buscar por el nombre del cliente y comida
    list_filter = ('estado', 'fecha_pedido')  # Filtrar por estado y fecha de pedido

    def cliente(self, obj):
        return obj.cliente.nombre  # Devuelve el nombre del cliente

    cliente.short_description = 'Nombre del Cliente'  # Encabezado personalizado

