from rest_framework import serializers
from proyecto_ips_app.models.especialidad import Especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Especialidad
        fields='__all__'