from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def crear_medico(request):
    if request.method == 'POST':
        formulario=MedicoFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            medico.set_password(formulario.cleaned_data['password'])
            medico.save()
            messages.success(request,'Medico creado exitosamente')
            return redirect('crear_medico')
        else:
            messages.error(request,'Hay errores en el registro. Vuelva e intentelo')
    else:
        formulario = MedicoFormulario()
        
    return render(request,'medico/insertar.html',{'formulario': formulario})

def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/listar.html', {'medicos':medicos})

def detallar_medico(request,id):
    medicos = get_object_or_404(Medico, id=id)
    return render(request,'medico/detallar.html',{'medico':medicos})

@login_required
def ver_perfil_medico(request):
    medicos = request.user.medico  # Ver el perfil del médico
    return render(request, 'medico/detallar.html', {'medico': medicos})


@login_required
def actualizar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == "POST":
        formulario = MedicoFormulario(request.POST, instance=medico)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se la cifra antes de pasarla al objeto medico
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                medico.set_password(nueva_password)
            medico.save()
            messages.success(request, 'Medico actualizado exitosamente.')
            return redirect('listar_medico')
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = MedicoFormulario(instance=medico)
    return render(request, 'medico/actualizar.html', {'formulario': formulario})
        

def eliminar_medico(request,id):
    medico=get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('listar_medico')