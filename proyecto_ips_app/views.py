from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash,login, logout, authenticate
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *


# Create your views here.
#region Login
#Menu principal
# @login_required
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
#endregion
# region usuario

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

#region Paciente
#Metodos de Paciente
# @login_required
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

#region Aux Administrativo

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
    
# region Medico
#Metodos de Medico   
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

#region Cita Medica
#Metodos de cita medica


def agendar_cita(request):
    if request.method == 'POST':
        form = CitaMedicaFormulario(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Cita agendada con éxito.")
                return redirect('agendar_cita')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CitaMedicaFormulario()
    
    return render(request, 'agendar_cita.html', {'form': form})

def actualizar_cita(request, id):
    cita = get_object_or_404(CitaMedica, id=id)

    if request.method == "POST":
        form_cita = CitaMedicaFormulario(request.POST, instance=cita)

        if form_cita.is_valid():
            # Guardamos la cita actualizada
            cita = form_cita.save()

            messages.success(request, 'Cita actualizada y formularios creados exitosamente.')
            return redirect('detallar_cita', id=id)
        else:
            messages.error(request, 'Hay errores en los formularios. Verifica los datos.')

    else:
        form_cita = CitaMedicaFormulario(instance=cita)


    return render(request, 'cita/actualizar.html', {
        'form_cita': form_cita,
        'cita': cita  # por si lo necesitás en el template
    })

# def detallar_cita(request,id):
#     citas = get_object_or_404(CitaMedica, id=id)
#     return render(request, 'cita/detallar.html', {
#         'citas': citas
#     })
def detallar_cita(request, id):
    cita = get_object_or_404(CitaMedica, id=id)
    return render(request, 'cita/detallar.html', {'citas': [cita]})



def listar_citas(request):
    citas = CitaMedica.objects.all()
    return render(request, 'cita/listar.html', {'citas':citas})

#region Especialidad
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

def eliminar_especialidad(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, id=especialidad_id)
    especialidad.delete()
    return redirect(listar_especialidad)
#endregion


#region Consultorio

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
    
#endregion 

#region Grupo Ingresos

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

#endregion 

#region Estado Cita

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

#endregion

#region Lugar Atencion 

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

#endregion

