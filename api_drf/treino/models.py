from django.db import models

from core.base_model import BaseModel
from usuario.models import Usuario
from momento_treino.models import MomentoTreino
from exercicio.models import Exercicio


class Treino(BaseModel):
	titulo = models.CharField(max_length=30)
	id_momento_treino = models.ForeignKey(MomentoTreino, on_delete=models.CASCADE)
	cpf_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	exercicios = models.ManyToManyField(Exercicio)	
	
	def __str__(self) -> str:
		return self.titulo

	class Meta:
		db_table = 'treino'

