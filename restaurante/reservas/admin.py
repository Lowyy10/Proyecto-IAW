from django.contrib import admin
from .models import Peticion, Reserva

class PeticionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'numero_personas')
    search_fields = ('nombre',)
    list_filter = ('fecha',)
    ordering = ('fecha',)

    class Meta:
        verbose_name = "Petición"
        verbose_name_plural = "Peticiones"


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('peticion', 'estado')
    list_filter = ('estado',)
    ordering = ('peticion__fecha',)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(Reserva, ReservaAdmin)
