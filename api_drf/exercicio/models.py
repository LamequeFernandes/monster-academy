from enum import Enum

from django.db import models

from enumchoicefield import EnumChoiceField

from core.base_model import BaseModel


class NivelDificuldadeEnum(Enum):
    FACIL = 'FACIL'
    MEDIO = 'MEDIO'
    DIFICIL = 'DIFICIL'

class Exercicio(BaseModel):
    nome = models.CharField(max_length=30)
    detalhe = models.TextField(max_length=500)
    repeticoes = models.IntegerField()
    temp_descanso = models.IntegerField()
    nivel_dificuldade = EnumChoiceField(NivelDificuldadeEnum)

    class Meta:
        db_table = 'exercicio'

