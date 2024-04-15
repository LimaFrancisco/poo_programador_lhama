from typing import Type

class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrebome = "Silva"

    def comer(self) ->  None:
        print("Estou comendo...")

    def estudar(self) -> None:
        print("Estou estudando...")


class Filha (Mae):

    def __init__(self, endereco) -> None:
        super().__init__(endereco) # metodos publicos passados para a classe filha

    def brincar(self, brinquedo: Type[str]) -> None:
        print(f"Estou brincando com o(a) {brinquedo}") 


class Neta (Filha):

    def __init__(self, endereco) -> None:
        super().__init__(endereco)


ana = Mae("Rua Elvira")
clara = Filha("Rua do Bolo")
clara.brincar("Boneca")

print(ana.endereco)
print(clara.endereco)
