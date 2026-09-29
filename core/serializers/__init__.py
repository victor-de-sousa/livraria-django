from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, 
    CompraSerializer, 
    ItensCompraUpdateSerializer,
    ItensCompraListSerializer, 
    ItensCompraSerializer,
)

from .editora import EditoraSerializer
from .livro import (
    LivroAjustarEstoqueSerializer,
    LivroAlterarPrecoSerializer,
    LivroMaisVendidoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer
)
from .user import UserRegistrationSerializer, UserSerializer