from django.contrib import admin
from .models import Platos, Pedidos, PedidoPlato, CatalogoPlatos, Ingrediente, Tipo_ingrediente, Bebidas, Tipo_bebida, Tipo_comida

class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display = ('tipo_ingrediente',)  # Mostrar el nombre del tipo de ingrediente en la lista
    search_fields = ('tipo_ingrediente',)

class TipoComidaAdmin(admin.ModelAdmin):
    list_display = ('tipo_comida',)  # Mostrar el nombre del tipo de ingrediente en la lista
    search_fields = ('tipo_comida',)

class TipobebidaAdmin(admin.ModelAdmin):
    list_display = ('tipo_bebida',)  # Mostrar el nombre del tipo de ingrediente en la lista
    search_fields = ('tipo_bebida',)

class BebidaAdmin(admin.ModelAdmin):
    list_display = ('nom_bebida', 'precio_bebida', 'mostrar_tipos_bebida','image')  # Añadido 'mostrar_tipos_bebida'
    search_fields = ('nom_bebida',)

    def mostrar_tipos_bebida(self, obj):
        return ", ".join([tipo.tipo_bebida for tipo in obj.tipo_bebi.all()])
    mostrar_tipos_bebida.short_description = "Tipos de Bebida"

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_ingrediente', 'tipo') # Mostrar el nombre del ingrediente y su tipo
    search_fields = ('nombre_ingrediente',)  # Permite buscar ingredientes por nombre

class PedidoPlatoInline(admin.TabularInline):
    model = PedidoPlato
    extra = 1  # Número de formularios adicionales a mostrar

class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio_plato', 'tipo_comida', 'mostrar_ingredientes')  # Mostrar tipo de comida
    search_fields = ('nombre_plato',)
    filter_horizontal = ('ingredientes',)

    def mostrar_ingredientes(self, obj):
        return ", ".join([ingrediente.nombre_ingrediente for ingrediente in obj.ingredientes.all()])
    mostrar_ingredientes.short_description = 'Ingredientes'

    
    mostrar_ingredientes.short_description = 'Ingredientes'  # Nombre de la columna en el admin
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona',)
    inlines = [PedidoPlatoInline]  # Añadir inlines para gestionar los platos y cantidades

    def total_precio(self, obj):
        return obj.total_precio()
    total_precio.short_description = 'Precio Total'

class CatalogoPlatosAdmin(admin.ModelAdmin):
    list_display = ('plato', 'precio_plato', 'valoracion', 'comentarios')
    list_filter = ('valoracion',)
    search_fields = ('plato__nombre_plato',)  # Asegúrate de que este campo es correcto

# Registro de los modelos
admin.site.register(Tipo_ingrediente, TipoIngredienteAdmin)  # Registro de Tipo_ingrediente
admin.site.register(Ingrediente, IngredienteAdmin)  # Registro de Ingrediente
admin.site.register(Platos, PlatosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(Bebidas, BebidaAdmin)
admin.site.register(CatalogoPlatos, CatalogoPlatosAdmin)
admin.site.register(Tipo_bebida, TipobebidaAdmin)
admin.site.register(Tipo_comida, TipoComidaAdmin)


