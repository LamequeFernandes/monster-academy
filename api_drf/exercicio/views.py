from rest_framework import viewsets

from .serializers import ExercicioSerializer
from .models import Exercicio


class ExercicioViewSet(viewsets.ModelViewSet):
    serializer_class = ExercicioSerializer
    queryset = Exercicio.objects.all()