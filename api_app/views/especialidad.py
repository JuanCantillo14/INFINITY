from rest_framework import viewsets
from proyecto_ips_app.models.especialidad import Especialidad
from api_app.serializers.especialidad import EspecialidadSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    
    queryset=Especialidad.objects.all()
    serializer_class=EspecialidadSerializer