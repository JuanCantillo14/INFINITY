from rest_framework import viewsets
from proyecto_ips_app.models.cita_medica import Cita
from api_app.serializers.cita_medica import CitaMedicaSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    
    queryset=Cita.objects.all()
    serializer_class=CitaMedicaSerializer