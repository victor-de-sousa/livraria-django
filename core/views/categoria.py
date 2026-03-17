from rest_framework.viewsets import ModelViewSet;

from core.serializers.categoria import CategoriaSerializer;
from core.models.categoria import Categoria;

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
