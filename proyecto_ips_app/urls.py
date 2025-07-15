from django.contrib import admin
from django.urls import path,include
from proyecto_ips_app.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',website, name='website'),
    path('home/',home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    #region Usuario
    path('usuario/registrar/', registrar_usuario, name='registrar_usuario'),
    path('usuario/eliminar/<int:usuario_id>', eliminar_usuario, name='eliminar_usuario'),
    path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
    path('usuario/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    path('usuario/mi_perfil/', mi_perfil_usuario, name='mi_perfil_usuario'),
    path('usuario/ver-perfil/', ver_perfil_usuario, name='perfil_usuario'),
    path('usuario/login/', login_usuario, name='login_usuario'),
    path('usuario/logout/', logout_usuario, name='logout_usuario'),
    #endregion 

    #region Paciente
    path('paciente/insertar/',crear_paciente, name='crear_paciente'),
    path('paciente/listar/',listar_paciente,name='listar_paciente'),
    path('paciente/detallar/<int:id>/',detallar_paciente, name='detallar_paciente'),
    path('paciente/actualizar/<int:id>/', actualizar_paciente, name='actualizar_paciente'),
    path('paciente/eliminar/<int:id>/',eliminar_paciente,name='eliminar_paciente'),
    path('paciente/mis_citas/',mis_citas_medicas,name='mis_citas_medicas'),
    #endregion
    
    #region Medico
    path('medico/insertar/',crear_medico, name='crear_medico'),
    path('medico/listar/',listar_medico,name='listar_medico'),
    path('medico/detallar/<int:id>/',detallar_medico, name='detallar_medico'),
    path('medico/actualizar/<int:id>/', actualizar_medico, name='actualizar_medico'),
    path('medico/eliminar/<int:id>/',eliminar_medico,name='eliminar_medico'),
    path('medico/ver-perfil/', ver_perfil_medico, name='perfil_medico'),
    path('medico-filtrar/listar/',listar_pacientes_filtrados,name='listar_pacientes_filtrados'),
    path('medico/medico/', citas_medico, name='citas_medico'),
    #endregion
    
    #region Aux Admin
    path('aux_admin/insertar/',crear_aux_admin, name='crear_aux_admin'),
    path('aux_admin/listar/',listar_aux_admin,name='listar_aux_admin'),
    path('aux_admin/detallar/<int:id>/',detallar_aux_admin, name='detallar_aux_admin'),
    path('aux_admin/actualizar/<int:id>/', actualizar_aux_admin, name='actualizar_aux_admin'),
    path('aux_admin/ver-perfil/', ver_perfil_aux_admin, name='perfil_aux_admin'),
    path('aux_admin/eliminar/<int:id>/',eliminar_aux_admin,name='eliminar_aux_admin'),
    #endregion

    #region Cita Medica
    path('cita/agendar/', agendar_cita, name='agendar_cita'),
    path('cita/crear/', crear_cita, name='crear_cita'),
    path('citas/mis/', mis_citas, name='mis_citas'),
    path('cita/cancelar/<int:cita_id>/', cancelar_cita, name='cancelar_cita'),
    path('cita/citas_auxiliar/', citas_auxiliar, name='listar_citas'),
    # path('cita/detallar/<int:id>/', detallar_cita, name='detallar_cita'),
    
    #endregion
        
    #region Especializacion 
    path('especialidad/insertar/', crear_especialidad,name='crear_especialidad'),
    path('especialidad/listar/', listar_especialidad,name='listar_especialidad'),
    path('especialidad/eliminar/<int:id>/', eliminar_especialidad,name='eliminar_especialidad'),
    #endregion

    
    #region Estado Cita
    path('estado_cita/insertar/', CrearEstadoCitaView.as_view(), name='crear_estado_cita'),
    path('estado_cita/listar/', ListarEstadoCitaView.as_view(), name='listar_estado_cita'),
    path('estado_cita/editar/<int:pk>/', EditarEstadoCitaView.as_view(), name='editar_estado_cita'),
    path('estado_cita/eliminar/<int:pk>/', EliminarEstadoCitaView.as_view(), name='eliminar_estado_cita'),
    #endregion 
    
    #region Lugar Atención 
    path('lugar_atencion/listar', ListarLugarAtencionView.as_view(), name='listar_lugar_atencion'),
    path('lugar_atencion/crear/', CrearLugarAtencionView.as_view(), name='crear_lugar_atencion'),
    path('lugar_atencion/editar/<int:pk>/', EditarLugarAtencionView.as_view(), name='editar_lugar_atencion'),
    path('lugar_atencion/eliminar/<int:pk>/', EliminarLugarAtencionView.as_view(), name='eliminar_lugar_atencion'),
    #endregion 
    
    #region Agenda
    path('agenda/nueva/', crear_agenda, name='crear_agenda'),
    path('agenda/listar/', listar_agenda, name='listar_agenda'),
    path('agenda/listar_aux/',listar_agenda_aux, name='listar_agenda_aux'),
    #endregion
    
    #region ERROR
    path('error/error_404/',error_404, name='error_404'),
    path('error/error_400/',error_400, name='error_400'),
    path('error/error_403/',error_403, name='error_403'),
    path('error/error_500/',error_500, name='error_500'),
    
    
    #region Ciudades
    path('ajax/ciudades/', cargar_ciudades, name='ajax_cargar_ciudades'),
    #endregion
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


