from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

class CrearGrupoIngresosView(CreateView):
    model = GrupoIngresos
    form_class = GrupoIngresosFormulario
    template_name = 'grupo_ingresos/insertar.html'
    success_url = reverse_lazy('listar_grupo_ingresos')  # redirige a la lista

    def form_valid(self, form):
        messages.success(self.request, 'Grupo Ingresos creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrió un error al crear el Grupo Ingresos.')
        return super().form_invalid(form)

class ListarGrupoIngresosView(ListView):
    model = GrupoIngresos
    template_name = 'grupo_ingresos/listar.html'
    context_object_name = 'grupo_ingresoss'

class EditarGrupoIngresosView(UpdateView):
    model = GrupoIngresos
    form_class = GrupoIngresosFormulario
    template_name = 'grupo_ingresos/actualizar.html'
    success_url = reverse_lazy('listar_grupo_ingresos')

    def form_valid(self, form):
        messages.success(self.request, 'Grupo Ingresos actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar el Grupo Ingresos.')
        return super().form_invalid(form)

class EliminarGrupoIngresosView(DeleteView):
    model = GrupoIngresos
    template_name = 'grupo_ingresos/eliminar.html'
    success_url = reverse_lazy('listar_grupo_ingresos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Grupo Ingresos eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
