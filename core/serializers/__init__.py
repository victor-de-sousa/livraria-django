from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer, 
    CompraSerializer, 
    ItensCompraUpdateSerializer, 
    ItensCompraSerializer,
)

from .editora import EditoraSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .user import UserRegistrationSerializer, UserSerializer