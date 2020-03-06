from rest_framework import viewsets

from tutorialpress.core.models import Categoria
from tutorialpress.core.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
