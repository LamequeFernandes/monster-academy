from enum import Enum

from django.db import models

from enumchoicefield import EnumChoiceField

from core.base_model import BaseModel
from usuario.models import Usuario


class DiaSemanaEnum(Enum):
    SEGUNDA = 'SEGUNDA'
    TERCA = 'TERCA'
    QUARTA = 'QUARTA'
    QUINTA = 'QUINTA'
    SEXTA = 'SEXTA'
    SABADO = 'SABADO'
    DOMINGO = 'DOMINGO'


class MomentoTreino(BaseModel):
    dia_semana = EnumChoiceField(DiaSemanaEnum)
    horario_inicio = models.TimeField(auto_now=False, auto_now_add=False)
    horario_fim = models.TimeField(auto_now=False, auto_now_add=False)
    cpf_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self

    class Meta:
        db_table = 'momento_treino'

