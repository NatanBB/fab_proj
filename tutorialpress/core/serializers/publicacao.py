from rest_framework import serializers

from tutorialpress.core.models import Publicacao


class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ["id", "titulo", "conteudo", "is_publicada", "categoria"]


class PublicacaoDetailSerializer(PublicacaoSerializer):
    categoria = serializers.CharField(source="categoria.nome", default="Root")
