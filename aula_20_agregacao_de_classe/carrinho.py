from typing import Type
from interface import Item

class CarrinhoDeCompras:

    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Item]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print("Compras finalizadas")

        for produto in self.__produtos:
            produto.informacoes_produto()

        self.__produtos = []