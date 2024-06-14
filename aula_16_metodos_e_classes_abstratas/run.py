from abs_class import AbastractClass

class Filha(AbastractClass):

    def apresentar_method(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print("Implementando metodo abstrado")


filha = Filha()
filha.apresentar_method()
filha.metodo("Estou aqui")
filha.metodo_abstrato()

# Error
# abastractClass = AbastractClass()
# abastractClass.metodo("Fazendo algo")
