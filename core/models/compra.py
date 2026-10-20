from xml.etree.ElementInclude import default_loader

from django.db import models

from .user import User

from .livro import Livro

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, 'Cartão de Crédito'
        CARTAO_DEBITO = 2, 'Cartão de Débito'
        PIX = 3, 'PIX'
        BOLETO = 4, 'Boleto'
        TRANSFERENCIA_BANCARIA = 5, 'Transferência Bancária'
        DINHEIRO = 6, 'Dinheiro'
        CHEQUE = 7, 'Cheque'
        OUTRO = 8, 'Outro'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    tipo_pagamento = models.IntegerField(
        choices=TipoPagamento.choices,
        default=TipoPagamento.PIX
    )
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # @property
    # def total(self):
    #    return sum(item.preco * item.quantidade for item in self.itens.all())

    def save(self, *args, **kwargs):
        if self.pk:
            self.total = sum(item.preco * item.quantidade for item in self.itens.all())
        super().save(*args, **kwargs)


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='itens_compra')
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
