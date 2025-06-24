from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def crear_aux_admin(request):
    if request.method=='POST':
        formulario= AuxAdminFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            aux_admin=formulario.save(commit=False)
            #contraseña encriptada :)
            aux_admin.set_password(formulario.cleaned_data['password'])
            aux_admin.save()
            messages.success(request, 'Auxiliar Administrativo registrado en el sistema éxitosamente')
            return redirect('crear_aux_admin')
        else:
            messages.error(request, 'Se encontraron errores en el registro. Vuelva a intentarlo')
    else: 
        formulario= AuxAdminFormulario()
    return render(request, 'aux_admin/insertar.html',{'formulario':formulario})


def listar_aux_admin(request):
    aux_admins = AuxAdmin.objects.all()
    return render(request, 'aux_admin/listar.html', {'aux_admins':aux_admins})

def detallar_aux_admin(request,id):
    aux_admins=get_object_or_404(AuxAdmin,id=id)
    return render(request,'aux_admin/detallar.html',{'aux_admin':aux_admins})

@login_required
def actualizar_aux_admin(request, id):
    aux_admin = get_object_or_404(AuxAdmin, id=id)
    if request.method == "POST":
        formulario = AuxAdminFormulario(request.POST, instance=aux_admin)
        if formulario.is_valid():
            aux_admin = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se la cifra antes de pasarla al objeto medico
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                aux_admin.set_password(nueva_password)
            aux_admin.save()
            messages.success(request, 'Aux Admin actualizado exitosamente.')
            return redirect('listar_aux_admin')
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = AuxAdminFormulario(instance=aux_admin)
    return render(request, 'aux_admin/actualizar.html', {'formulario': formulario})

@login_required
def ver_perfil_aux_admin(request):
    aux_admins = request.user.auxadmin  # Ver página el perfil del usuario
    return render(request, 'aux_admin/detallar.html', {'aux_admin': aux_admins})

def eliminar_aux_admin(request,id):
    aux_admin=get_object_or_404(AuxAdmin, id=id)
    aux_admin.delete()
    return redirect('listar_aux_admin')