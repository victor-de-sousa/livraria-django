from rest_framework.viewsets import ModelViewSet
from core.models.editora import Editora
from core.serializers.editora import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer