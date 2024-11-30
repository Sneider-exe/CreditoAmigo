from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_llegada = models.DateTimeField()
    hora_llegada = models.TimeField(default='00:00:00')
    matricula_vehiculo = models.CharField(max_length=50)
    tiempo_requerido = models.CharField(max_length=50)
    necesita_restaurante = models.BooleanField(default=False)
    necesita_mantenimiento = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.fecha_llegada}"
