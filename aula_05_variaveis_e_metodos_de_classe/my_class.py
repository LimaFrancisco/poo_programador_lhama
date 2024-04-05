class MinhaClasse: 

    estatico = "lhama" # pode ser usado no contexto da classe ou do objeto

    def __init__(self, estado):
        self.estado = estado
        self.estatico = "lhama"

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Programador"

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj2.print_estatico()
obj1.print_estatico()

# O contexto da classe é passado para os objetos mas o contexto dos objetos fica somente armazenado neles
