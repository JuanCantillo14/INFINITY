from rest_framework import serializers
from proyecto_ips_app.models.cita_medica import Cita

class CitaMedicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Cita
        fields='__all__'