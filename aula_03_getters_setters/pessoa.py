class Pessoa: # substantivo

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome # substantivo
        self.idade = idade # substantivo

    def dirigir(self, veiculo: str) -> None: # verbo
        print(f"Dirigindo um(a) {veiculo}")

    def cantar(self) -> None: # verbo
        print("Lalalala")
 
    def aprendentar_idade(self) -> int: # verbo
        return self.idade
     