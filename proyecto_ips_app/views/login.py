from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash,login, logout, authenticate
from django.contrib import messages
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def home(request):
    return render(request, 'home.html')

def inicio(request):
    tipo_usuario = None

    if request.user.is_authenticated:
        usuario_logueado = request.user
        if isinstance(usuario_logueado, Medico):
            tipo_usuario = 'Medico'
        elif isinstance(usuario_logueado, AuxAdmin):
            tipo_usuario = 'AuxAdmin'
        elif isinstance(usuario_logueado, Paciente):
            tipo_usuario = 'Paciente'
        else:
            tipo_usuario = 'Usuario no identificado'

    return render(request, 'inicio.html', {'tipo_usuario': tipo_usuario})

def login_usuario(request):
    if request.method == 'POST':
        username_recibido = request.POST.get('username')
        password_recibido = request.POST.get('password')
        
        if not username_recibido or not password_recibido:
            return render(request, 'usuario/login.html', {'mensaje_error': 'Por favor, complete todos los campos.'})
        
        usuario = authenticate(request, username=username_recibido, password=password_recibido)
        
        if usuario is not None:
            login(request, usuario)
            
            # Verificar el tipo de usuario
            if Medico.objects.filter(id=usuario.id).exists():
                return render(request, 'medico/perfil.html', {'tipo_usuario': 'Medico'})
            elif AuxAdmin.objects.filter(id=usuario.id).exists():
                return render(request, 'aux_admin/perfil.html', {'tipo_usuario': 'Aux_Admin'})
            elif Paciente.objects.filter(id=usuario.id).exists():
                return render(request, 'paciente/perfil.html', {'tipo_usuario': 'Paciente'})
            else:
                messages.error(request, 'El usuario no tiene un rol válido asignado.')
                return redirect('home')
                
        return render(request, 'usuario/login.html', {'mensaje_error': 'Credenciales incorrectas, intente de nuevo.'})

    return render(request, 'usuario/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('home')