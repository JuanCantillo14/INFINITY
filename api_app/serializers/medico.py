
from rest_framework import serializers
from proyecto_ips_app.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Medico
        fields='__all__'