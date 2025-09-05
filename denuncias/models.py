from django.db import models
from django.contrib.auth.models import User

class Denuncia(models.Model):
    TIPO_ACOSO = [
        ('laboral', 'Acoso Laboral'),
        ('sexual', 'Acoso Sexual'),
        ('discriminacion', 'Discriminación'),
    ]

    ESTADOS = [
        ('ingresada', 'Ingresada'),
        ('investigacion', 'En Investigación'),
        ('resuelta', 'Resuelta'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_ACOSO)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ingresada')
    anonima = models.BooleanField(default=False)

    def __str__(self):
        return f"Denuncia de {self.usuario.username} - {self.tipo}"