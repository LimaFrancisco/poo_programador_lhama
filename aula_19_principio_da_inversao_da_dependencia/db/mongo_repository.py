from .interface import Repositorio

class MongoRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f"Inserindo {dado} no banco Mongo")

    def deletar(self, dado) -> None:
        print(f"deletando {dado} no banco Mongo")