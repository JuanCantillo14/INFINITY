from rest_framework import viewsets
from proyecto_ips_app.models.consultorio import Consultorio
from api_app.serializers.consultorio import ConsultorioSerializer

class ConsultorioViewSet(viewsets.ModelViewSet):
    
    queryset=Consultorio.objects.all()
    serializer_class=ConsultorioSerializer