from enum import Enum, unique
import gc
from django.db import models
from django.core.validators import MinLengthValidator
from enumchoicefield import EnumChoiceField


class ObjetivosEnum(Enum):
    GANHAR = 'GANHAR'
    MANTER = 'MANTER'
    PERDER = 'PERDER'


class Usuario(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11, validators=[MinLengthValidator(11)])
    is_admin = models.BooleanField(default=False)
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(max_length=247, unique=True)
    senha = models.CharField(max_length=247)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    altura = models.IntegerField(blank=True)
    dt_nascimento = models.DateField()
    objetivo = EnumChoiceField(ObjetivosEnum)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.nome_completo

    class Meta:
        db_table = 'usuario'
