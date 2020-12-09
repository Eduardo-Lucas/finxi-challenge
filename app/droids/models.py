from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Peca(models.Model):
    codigo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    importada = models.CharField(max_length=3, default='Não')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao}"
