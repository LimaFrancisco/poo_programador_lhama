class MinhaClasse:

    def __init__(self, estado: bool) -> None:
        self.estado = estado

    @staticmethod
    def metodo_estatico():
        #print(self.estado) # Não possui contexto definido
        print("Estou no metodo estatico :D")

