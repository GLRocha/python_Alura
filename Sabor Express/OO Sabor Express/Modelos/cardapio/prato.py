from modelos.cardapio.item_cardapio import ItemCardapio # type: ignore

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome