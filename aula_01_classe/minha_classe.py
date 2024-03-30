class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("Canal Avancado")

    def voltar_canal(self):
        print("Voltar o Canal")

    def escolher_canal(self, canal):
        print(f"O canal escolhido foi: {canal}")

controle_sala = ControleRemoto("samsung", "sala")
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(8)

controle_quarto = ControleRemoto("Lg", "quarto")
print(controle_quarto.comodo)
print(controle_quarto.televisao)
