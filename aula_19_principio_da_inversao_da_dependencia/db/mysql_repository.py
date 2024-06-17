from .interface import Repositorio

class MySqlRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f"Inserindo {dado} no banco Mysql")

    def deletar(self, dado) -> None:
        print(f"deletando {dado} no banco Mysql")