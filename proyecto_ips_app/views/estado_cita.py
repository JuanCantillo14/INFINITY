from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

class CrearEstadoCitaView(CreateView):
    model = EstadoCita
    form_class = EstadoCitaFormulario
    template_name = 'estado_cita/insertar.html'
    success_url = reverse_lazy('listar_estado_cita')  # redirige a la lista

    def form_valid(self, form):
        messages.success(self.request, 'Estado Cita creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al crear el Estado Cita.')
        return super().form_invalid(form)

class ListarEstadoCitaView(ListView):
    model = EstadoCita
    template_name = 'estado_cita/listar.html'
    context_object_name = 'estado_citas'

class EditarEstadoCitaView(UpdateView):
    model = EstadoCita
    form_class = EstadoCitaFormulario
    template_name = 'estado_cita/actualizar.html'
    success_url = reverse_lazy('listar_estado_cita')

    def form_valid(self, form):
        messages.success(self.request, 'Estado Cita actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar el Estado Cita.')
        return super().form_invalid(form)

class EliminarEstadoCitaView(DeleteView):
    model = EstadoCita
    template_name = 'estado_cita/eliminar.html'
    success_url = reverse_lazy('listar_estado_cita')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Estado Cita eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
