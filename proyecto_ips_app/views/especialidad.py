from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def crear_especialidad(request):
    if request.method == 'POST':
        formulario = EspecialidadFormulario(request.POST)
        if formulario.is_valid():
            especialidad = formulario.save(commit=False)
            especialidad.save()
            messages.success(request, 'Especialidad médica creada exitosamente.')
            return redirect('listar_especialidad')
        else:
            messages.error(request, 'Revise los errores y continue.')
    else:
        formulario = EspecialidadFormulario()
    return render(request, 'especialidad/insertar.html', {'formulario': formulario})

def actualizar_especialidad(request, id):
    especialidad = get_object_or_404(Especialidad, id=id)
    if request.method == "POST":
        formulario = EspecialidadFormulario(request.POST, instance=especialidad)
        if formulario.is_valid():
            especialidad = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se la cifra antes de pasarla al objeto medico
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                especialidad.set_password(nueva_password)
            especialidad.save()
            messages.success(request, 'Especialidad actualizada exitosamente.')
            return redirect('detallar_especialidad', id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = EspecialidadFormulario(instance=especialidad)
    return render(request, 'espe/actualizar.html', {'formulario': formulario})

def listar_especialidad(request): 
    especialidades = Especialidad.objects.all()
    return render(request, 'especialidad/listar.html', {'especialidades':especialidades})

def eliminar_especialidad(request, id):
    especialidad = get_object_or_404(Especialidad, pk=id)
    especialidad.delete()
    return redirect(listar_especialidad)