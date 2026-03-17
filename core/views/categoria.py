from rest_framework.viewsets import ModelViewSet

from core.models.categoria import Categoria
from core.serializers.categoria import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
