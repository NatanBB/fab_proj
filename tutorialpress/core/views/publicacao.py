from rest_framework import viewsets

from tutorialpress.core.models import Publicacao
from tutorialpress.core.serializers import PublicacaoDetailSerializer, PublicacaoSerializer


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    lookup_field = "id"
    # serializer_class = PublicacaoSerializer

    def get_serializer(self):
        if self.action == "list" or self.action == "retrieve":
            return PublicacaoDetailSerializer()
        else:
            return PublicacaoSerializer()
