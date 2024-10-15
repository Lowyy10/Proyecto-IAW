from django.contrib import admin
from .models import Platos, Pedidos, PedidoPlato, CatalogoPlatos, Ingrediente

class PedidoPlatoInline(admin.TabularInline):
    model = PedidoPlato
    extra = 1  # Número de formularios adicionales a mostrar

class IngredientesAdmin(admin.ModelAdmin):
    display = ('nombre_ingrediente')

class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio_plato')
    search_fields = ('nombre_plato',)
    filter_horizontal = ('ingredientes',)  # Permite seleccionar múltiples ingredientes

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
admin.site.register(Platos, PlatosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(CatalogoPlatos, CatalogoPlatosAdmin)
admin.site.register(Ingrediente, IngredientesAdmin)
