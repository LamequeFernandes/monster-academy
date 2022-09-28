from enum import Enum

from django.db import models

from enumchoicefield import EnumChoiceField

from uuid import uuid4


class NivelDificuldadeEnum(Enum):
    FACIL = 'FACIL'
    MEDIO = 'MEDIO'
    DIFICIL = 'DIFICIL'

class Exercicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=30)
    detalhe = models.TextField(max_length=500)
    repeticoes = models.IntegerField()
    temp_descanso = models.IntegerField()
    nivel_dificuldade = EnumChoiceField(NivelDificuldadeEnum)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'exercicio'

