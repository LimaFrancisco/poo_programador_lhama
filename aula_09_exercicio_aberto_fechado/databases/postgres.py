class PostgresBD:

    def __init__(self) -> None:
        self.__conexao = "Postgres"

    def conectar(self) -> str:
        print("Conectando ao banco Postgres...")
        return self.__conexao
    
    def desconectar(self) -> None:
        print("Desconectando ao banco Postgres...")