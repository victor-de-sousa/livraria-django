from rest_framework.serializers import ModelSerializer
from core.models.editora import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'