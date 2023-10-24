from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos", null=True)
    
    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    TIPO_CHOICES = [
        ("S","Suspensión de actividades"),
        ("C", "Suspensión de clase"),
        ("I", "Información")
    ]
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=1000)
    detalle_corto = models.CharField(max_length=500)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicados_por')
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE,related_name='modificador_por')

    def __str__(self) -> str:
        return self.titulo