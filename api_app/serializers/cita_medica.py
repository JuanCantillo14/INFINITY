from rest_framework import serializers
from proyecto_ips_app.models.cita_medica import CitaMedica

class CitaMedicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= CitaMedica
        fields='__all__'