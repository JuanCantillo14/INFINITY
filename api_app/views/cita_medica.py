from rest_framework import viewsets
from proyecto_ips_app.models.cita_medica import CitaMedica
from api_app.serializers.cita_medica import CitaMedicaSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    
    queryset=CitaMedica.objects.all()
    serializer_class=CitaMedicaSerializer