from dataclasses import field
from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioParcialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        field = '__all__'
        exclude = ['senha']