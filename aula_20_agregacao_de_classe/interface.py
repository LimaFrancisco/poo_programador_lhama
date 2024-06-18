from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def informacoes_produto(self) -> None:
        pass