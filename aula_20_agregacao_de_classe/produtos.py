from interface import Item

class Produto(Item):

    def __init__(self, prod_nome: str, prod_valor: int) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor

    def informacoes_produto(self) -> None:
        print(f"Produto: {self.__prod_nome} / valor: R$ {self.__prod_valor},00")
        