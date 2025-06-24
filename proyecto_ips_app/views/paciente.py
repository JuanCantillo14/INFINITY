from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def crear_paciente(request):
    if request.method=='POST':
        formulario= PacienteFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            paciente=formulario.save(commit=False)
            #contraseña encriptada :)
            paciente.set_password(formulario.cleaned_data['password'])
            paciente.save()
            messages.success(request, 'Paciente registrado en el sistema éxitosamente')
            return redirect('crear_paciente')
        else:
            messages.error(request, 'Se encontraron errores en el registro. Vuelva a intentarlo')
    else: 
        formulario= PacienteFormulario()
    return render(request, 'paciente/insertar.html',{'formulario':formulario})

def listar_paciente(request): 
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/listar.html', {'pacientes':pacientes})

def detallar_paciente(request,id):
    pacientes=get_object_or_404(Paciente,id=id)
    return render(request,'paciente/detallar.html',{'paciente':pacientes}) 

def actualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST, instance=paciente)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se la cifra antes de pasarla al objeto medico
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                paciente.set_password(nueva_password)
            paciente.save()
            messages.success(request, 'paciente actualizado exitosamente.')
            return redirect('detallar_paciente', id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = PacienteFormulario(instance=paciente)
    return render(request, 'paciente/actualizar.html', {'formulario': formulario})

def eliminar_paciente(request,id):
    paciente=get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_paciente')

@login_required
def mis_citas_medicas(request):
    # Como Paciente hereda de Usuario, el request.user ES un Paciente
    paciente = request.user  # Aquí no necesitas buscar en el modelo Paciente

    citas = CitaMedica.objects.filter(paciente=paciente).order_by('dia', 'horario')

    if not citas:
        messages.info(request, "No tienes citas médicas asignadas.")

    return render(request, 'paciente/mis_citas.html', {'citas': citas})
