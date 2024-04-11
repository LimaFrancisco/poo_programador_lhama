class Repositorio:

    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Me conectei ao banco {connection}")
        print("Fazendo um SLECT * FROM")
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Me conectei ao banco {connection}")
        print("Fazendo um insert values...")
        db_connection.desconectar()
