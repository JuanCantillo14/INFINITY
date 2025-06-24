from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

class CrearLugarAtencionView(CreateView):
    model = LugarAtencion
    form_class = LugarAtencionFormulario
    template_name = 'lugar_atencion/insertar.html'
    success_url = reverse_lazy('listar_lugar_atencion')  # redirige a la lista

    def form_valid(self, form):
        messages.success(self.request, 'Lugar de Atencion creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al crear el Lugar de Atencion.')
        return super().form_invalid(form)

class ListarLugarAtencionView(ListView):
    model = LugarAtencion
    template_name = 'lugar_atencion/listar.html'
    context_object_name = 'lugar_atenciones'

class EditarLugarAtencionView(UpdateView):
    model = LugarAtencion
    form_class = LugarAtencionFormulario
    template_name = 'lugar_atencion/actualizar.html'
    success_url = reverse_lazy('listar_lugar_atencion')

    def form_valid(self, form):
        messages.success(self.request, 'Lugar de Atencion actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar el Lugar de Atencion.')
        return super().form_invalid(form)

class EliminarLugarAtencionView(DeleteView):
    model = LugarAtencion
    template_name = 'lugar_atencion/eliminar.html'
    success_url = reverse_lazy('listar_lugar_atencion')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Lugar de Atencion eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
