from django.contrib.auth.models import Filme
from rest_framework import serializers

class FilmeSerializer(serializers, HyperlinkedModelSerializer):
    class Lista:
        model = Filme
        fields = ['nome', 'genero', 'duracao', 'descricao']