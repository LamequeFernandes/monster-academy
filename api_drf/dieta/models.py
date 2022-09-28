from statistics import mode
from django.db import models

from core.base_model import BaseModel
from usuario.models import Usuario


class Dieta(BaseModel):
    titulo = models.CharField(max_length=30)
    max_calorias_diarias = models.IntegerField()
    min_calorias_diarias = models.IntegerField()
    tipo = models.CharField(max_length=15, blank=True)
    cpf_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        db_table = 'dieta'
