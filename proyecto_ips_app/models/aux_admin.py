from django.db import models
from proyecto_ips_app.models.usuario import *

class AuxAdmin(Usuario):
    
    class Meta:
        db_table='aux_admin'
        
    def __str__(self):
        return self.first_name, self. last_name
    
        
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = True
            self.rol = 'AUX'
        super().save(*args, **kwargs)
    
