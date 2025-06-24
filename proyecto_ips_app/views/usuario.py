from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.save(commit=False) # Se crea un objeto usuario en memoria
            # Cifra la contraseña utilizando set_password()
            usuario.set_password(formulario.cleaned_data['password'])
            usuario.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('registrar_usuario')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = UsuarioFormulario()
    return render(request, 'usuario/insertar.html', {'formulario': formulario})

@login_required
def actualizar_usuario(request):
    usuario = request.user  # Usuario logueado

    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST, request.FILES, instance=usuario)  # Se incluye request.FILES
        
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # Aún no guardar en la BD
            nueva_password = formulario.cleaned_data.get('password')

            if nueva_password:
                usuario.set_password(nueva_password)

            # Si se subió una nueva imagen, actualizarla
            if 'imagen' in request.FILES:
                usuario.imagen = request.FILES['imagen']
            
            # Si el usuario dejó el campo de imagen en blanco, eliminar la imagen
            elif not formulario.cleaned_data.get('imagen'):
                usuario.imagen = None  

            usuario.save()  # Ahora sí guardamos todo en la BD
            update_session_auth_hash(request, usuario)  # Mantiene la sesión activa después de actualizar la contraseña            
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('perfil_usuario')

        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')

    else:
        formulario = UsuarioFormulario(instance=usuario)

    return render(request, 'usuario/actualizar.html', {'formulario': formulario})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar.html', {'usuarios':usuarios})

@login_required
def listar_pacientes_filtrados(request):
    consultaSQL = request.GET.get('consultaSQL', '').strip()  # Obtener y limpiar la consulta del usuario
    pacientes = None  # Inicializar la variable usuariosos
            
    if consultaSQL:  # Solo buscar si hay un valor en el campo
        pacientes = Paciente.objects.filter(Q(first_name__istartswith= consultaSQL)|Q(documento__istartswith=consultaSQL))
    
        if not pacientes:
            messages.info(request, "No se encontraron pacientes")  # Mensaje si no hay resultados

    return render(request, 'medico/buscar_paciente.html', {'pacientes': pacientes, 'consultaSQL': consultaSQL})


def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect(listar_usuarios)

@login_required
def ver_perfil_usuario(request):
    usuario = request.user.id  # Ver página el perfil del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario})

@login_required
def detallar_usuario(request):
    usuario = request.user.id  # Ver los detalles del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario })
