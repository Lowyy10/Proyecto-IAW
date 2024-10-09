from django.contrib import admin
from .models import Platos, Pedidos, PedidoPlato, CatalogoPlatos

class PedidoPlatoInline(admin.TabularInline):
    model = PedidoPlato
    extra = 1  # Número de formularios adicionales a mostrar

class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio_plato')
    search_fields = ('nombre_plato',)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona',)
    inlines = [PedidoPlatoInline]  # Añadir inlines para gestionar los platos y cantidades

    def total_precio(self, obj):
        return obj.total_precio()
    total_precio.short_description = 'Precio Total'

class CatalogoPlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio_plato', 'valoracion', 'comentarios')
    list_filter = ('valoracion',)
    search_fields = ('nombre_plato__nombre_plato',)

# Registro de los modelos
admin.site.register(Platos, PlatosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(CatalogoPlatos, CatalogoPlatosAdmin)