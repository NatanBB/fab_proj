from rest_framework import serializers

from tutorialpress.core.models import Publicacao


class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ["id", "titulo", "conteudo", "is_publicada"]
