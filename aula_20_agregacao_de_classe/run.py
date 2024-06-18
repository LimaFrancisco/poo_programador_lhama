from produtos import Produto
from servico import Servico
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto("Monitor", 1000)
cerveja = Produto("Cerveja", 5)
tv = Produto("TV", 1200)
entrega = Servico("Entrega", 30)
embalar = Servico("Embalar produto", 10)


car.adicionar_produto(monitor)
car.adicionar_produto(cerveja)
car.adicionar_produto(cerveja)
car.adicionar_produto(tv)
car.adicionar_produto(entrega)
car.adicionar_produto(embalar)
car.finalizar_compra()