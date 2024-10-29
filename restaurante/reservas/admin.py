from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Platos, Perfil, Ingrediente, Tipo_ingrediente, Bebidas, Tipo_bebida, Tipo_comida, MisPedidos

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

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

class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio_plato', 'tipo_comida', 'mostrar_ingredientes', 'valoracion', 'comentarios')  # Mostrar tipo de comida
    search_fields = ('nombre_plato',)
    filter_horizontal = ('ingredientes',)

    def mostrar_ingredientes(self, obj):
        return ", ".join([ingrediente.nombre_ingrediente for ingrediente in obj.ingredientes.all()])
    mostrar_ingredientes.short_description = 'Ingredientes'

    
    mostrar_ingredientes.short_description = 'Ingredientes'  # Nombre de la columna en el admin

    def total_precio(self, obj):
        return obj.total_precio()
    total_precio.short_description = 'Precio Total'
    
class MisPedidosAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona', 'mostrar_plato', 'cantidad', 'fecha_pedido')

    def mostrar_plato(self, obj):
        return obj.plato.nombre_plato
    mostrar_plato.short_description = 'Plato'


    def total_precio(self, obj):
        return obj.total_precio()
    total_precio.short_description = 'Precio Total'

# Registro de los modelos
admin.site.register(Tipo_ingrediente, TipoIngredienteAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Platos, PlatosAdmin)
admin.site.register(Bebidas, BebidaAdmin)
admin.site.register(Tipo_bebida, TipobebidaAdmin)
admin.site.register(Tipo_comida, TipoComidaAdmin)
admin.site.register(MisPedidos, MisPedidosAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



