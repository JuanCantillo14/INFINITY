from rest_framework import viewsets
from proyecto_ips_app.models.paciente import Paciente
from api_app.serializers.paciente import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    
    queryset=Paciente.objects.all()
    serializer_class=PacienteSerializer