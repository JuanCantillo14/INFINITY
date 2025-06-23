from rest_framework import serializers
from proyecto_ips_app.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Paciente
        fields='__all__'