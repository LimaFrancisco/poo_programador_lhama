from typing import Type

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print(f"acendendo {self.__comodo}")

    def apagar(self) -> None:
        print(f"apagando {self.__comodo}")


class Pessoa:

    def acender_lux(self, interruptor: Type[Interruptor]) -> None:
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print("Fui dormir...")


lhama = Pessoa()
interruptor_quarto = Interruptor("quarto")
interruptor_cozinha = Interruptor("cozinha")

interruptor_quarto.acender()
lhama.acender_lux(interruptor_cozinha)
lhama.apagar_luz(interruptor_quarto)
lhama.dormir()
