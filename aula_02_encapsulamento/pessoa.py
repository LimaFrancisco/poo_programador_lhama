class Pessoa: 

    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade
        self.__cpf = cpf # atributo privado

    def correr(self):
        print(f"{self.nome} esta correndo")

    def beber(self, bebida):
        if bebida == "cerveja":
            self.__apresentar_documento()
        print("bebendo")

    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa("Ronaldo", 32, 23123123123)
ronaldo.correr()
ronaldo.beber("cerveja")
ronaldo.beber("coca-cola")
