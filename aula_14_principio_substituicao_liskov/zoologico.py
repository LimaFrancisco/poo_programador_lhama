from typing import Type

class Animal:

    def comer(self):
        print("O animal esta comendo")

    def dormir(self):
        print("O animal esta dormindo")

    def andar(self):
        print("O animal esta andando")


class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self):
        print("A ave esta cantando")

        
class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self):
        print("O pinguim esta escorregando no gelo")


class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.andar()


roberto = Pessoa()
pinguim = Animal()
roberto.observar(pinguim)