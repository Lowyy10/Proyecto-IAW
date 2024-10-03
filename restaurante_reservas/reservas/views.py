from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Reserva
from .forms import ReservaForm

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reservas:crear_reserva')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Relaciona la reserva con el usuario actual
        return super().form_valid(form)
