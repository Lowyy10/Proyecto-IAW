from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'num_personas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegura que los campos de fecha y hora utilicen los widgets HTML adecuados
        self.fields['fecha'].widget.attrs.update({'class': 'datepicker', 'placeholder': 'Selecciona una fecha'})
        self.fields['hora'].widget.attrs.update({'class': 'timepicker', 'placeholder': 'Selecciona una hora'})
