from interface import Item
from typing import Type

class Servico(Item):

    def __init__(self, nome_serv: Type[str], valor_serv: Type[int]) -> None:
        self.__nome_serv = nome_serv
        self.__valor_serv = valor_serv

    def informacoes_produto(self) -> None:
        print(f"Produto: {self.__nome_serv} / valor: R$ {self.__valor_serv},00")