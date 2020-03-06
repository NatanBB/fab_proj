from rest_framework import viewsets

from tutorialpress.core.models import Publicacao
from tutorialpress.core.serializers import PublicacaoSerializer


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
