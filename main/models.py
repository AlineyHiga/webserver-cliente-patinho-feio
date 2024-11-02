# main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USUARIO_CHOICES = [
        ('AGRICULTOR', 'Agricultor'),
        ('CONSUMIDOR', 'Consumidor'),
    ]

    celular = models.CharField(max_length=15, blank=True)
    tipo_usuario = models.CharField(max_length=10, choices=USUARIO_CHOICES, null=True)

    class Meta:
        app_label = 'main'
