from django.db import models
from django.utils import timezone

from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)