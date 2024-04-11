class MySqlBD:

    def __init__(self) -> None:
        self.__conexao = "MySql"

    def conectar(self) -> str:
        print("Conectando ao banco MySql...")
        return self.__conexao
    
    def desconectar(self) -> None:
        print("Desconectando ao banco MySql...")