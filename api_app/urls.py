from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import *

router=DefaultRouter()

router.register(r'aux_admin',AuxAdminViewSet,basename='aux_admin')
router.register(r'cita_medicas',CitaMedicaViewSet,basename='cita_medica')
router.register(r'medicos',MedicoViewSet,basename='medico')
router.register(r'pacientes',PacienteViewSet,basename='paciente')
router.register(r'usuarios',UsuarioViewSet,basename='usuario')
router.register(r'especialidades',EspecialidadViewSet,basename='especialidad')
router.register(r'consultorios',ConsultorioViewSet,basename='consultorio')

urlpatterns=[
    path('',include(router.urls))
]

