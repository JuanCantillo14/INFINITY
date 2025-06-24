from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

class CrearConsultorioView(CreateView):
    model = Consultorio
    form_class = ConsultorioFormulario
    template_name = 'consultorio/insertar.html'
    success_url = reverse_lazy('listar_consultorio')  # redirige a la lista

    def form_valid(self, form):
        messages.success(self.request, 'Consultorio creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al crear el consultorio.')
        return super().form_invalid(form)

class ListarConsultorioView(ListView):
    model = Consultorio
    template_name = 'consultorio/listar.html'
    context_object_name = 'consultorios'

class EditarConsultorioView(UpdateView):
    model = Consultorio
    form_class = ConsultorioFormulario
    template_name = 'consultorio/actualizar.html'
    success_url = reverse_lazy('listar_consultorio')

    def form_valid(self, form):
        messages.success(self.request, 'Consultorio actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar el consultorio.')
        return super().form_invalid(form)

class EliminarConsultorioView(DeleteView):
    model = Consultorio
    template_name = 'consultorio/eliminar.html'
    success_url = reverse_lazy('listar_consultorio')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Consultorio eliminado correctamente.')
        return super().delete(request, *args, **kwargs)