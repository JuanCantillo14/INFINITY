from django.contrib import admin
from django.urls import path,include
from proyecto_ips_app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    #region Usuario
    path('usuario/registrar/', registrar_usuario, name='registrar_usuario'),
    path('usuario/eliminar/<int:usuario_id>', eliminar_usuario, name='eliminar_usuario'),
    path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
    path('usuario/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    path('usuario/detallar/', detallar_usuario, name='detallar_usuario'),
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
    path('cita/insertar/',agendar_cita, name='crear_cita'),
    path('cita/listar/',listar_citas,name='listar_citas'), 
    path('cita/actualizar/<int:id>/',actualizar_cita,name='actualizar_cita'),
    path('cita/detallar/<int:id>/', detallar_cita, name='detallar_cita'),
    # path('cita/detallar/<int:id>/', detallar_cita, name='detallar_cita'),
    
    #endregion
        
    #region Especializacion 
    path('especialidad/insertar/', crear_especialidad,name='crear_especialidad'),
    path('especialidad/listar/', listar_especialidad,name='listar_especialidad'),
    path('especialidad/eliminar/<int:id>/', eliminar_especialidad,name='eliminar_especialidad'),
    #endregion

    #region Consultorio Medico
    path('consultorio/insertar/',CrearConsultorioView.as_view(), name='crear_consultorio'),
    path('consultorio/listar/',ListarConsultorioView.as_view(), name='listar_consultorio'),
    path('consultorios/editar/<int:pk>/', EditarConsultorioView.as_view(), name='editar_consultorio'),
    path('consultorios/eliminar/<int:pk>/', EliminarConsultorioView.as_view(), name='eliminar_consultorio'),
    #endregion 

    #region Grupo Ingresos
    path('grupo_ingresos/insertar/',CrearGrupoIngresosView.as_view(), name='crear_grupo_ingresos'),
    path('grupo_ingresos/listar/',ListarGrupoIngresosView.as_view(), name='listar_grupo_ingresos'),
    path('grupo_ingresos/editar/<int:pk>/', EditarGrupoIngresosView.as_view(), name='editar_grupo_ingresos'),
    path('grupo_ingresos/eliminar/<int:pk>/', EliminarGrupoIngresosView.as_view(), name='eliminar_grupo_ingresos'),
    #endregion 
    
    #region Estado Cita
    path('estado_cita/insertar/', CrearEstadoCitaView.as_view(), name='crear_estado_cita'),
    path('estado_cita/listar/', ListarEstadoCitaView.as_view(), name='listar_estado_cita'),
    path('estado_cita/editar/<int:pk>/', EditarEstadoCitaView.as_view(), name='editar_estado_cita'),
    path('estado_cita/eliminar/<int:pk>/', EliminarEstadoCitaView.as_view(), name='eliminar_estado_cita'),
    #endregion 
    
    #region Lugar Atención 
    path('lugar_atencion/', ListarLugarAtencionView.as_view(), name='listar_lugar_atencion'),
    path('lugar_atencion/crear/', CrearLugarAtencionView.as_view(), name='crear_lugar_atencion'),
    path('lugar_atencion/editar/<int:pk>/', EditarLugarAtencionView.as_view(), name='editar_lugar_atencion'),
    path('lugar_atencion/eliminar/<int:pk>/', EliminarLugarAtencionView.as_view(), name='eliminar_lugar_atencion'),
    #endregion 

    #region Ciudades
    path('ajax/ciudades/', cargar_ciudades, name='ajax_cargar_ciudades'),
    #endregion
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



