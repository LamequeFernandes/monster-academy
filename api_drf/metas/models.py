from django.db import models

from core.base_model import BaseModel

from usuario.models import Usuario


class Meta(BaseModel):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500)
    cpf_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo
        
    class Meta:
        db_table = 'meta'