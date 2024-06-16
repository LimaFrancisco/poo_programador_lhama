from interface import AveVoadora, AveQueNaoVoa
class Canario(AveVoadora):

    def comer(self) -> None:
        print("Estou comendo!")

    def voar(self) -> None:
        print("Estou voando!")

    def gritar(self) -> None:
        print("Estou gritando")

class Pinguim(AveQueNaoVoa):

    def comer(self) -> None:
        print("Estou comendo!")
        self.__acasalar()

    def gritar(self) -> None:
        print("Estou gritando")

    def __acasalar(self) -> None:
        print("Agora vou acasalar...")
