class DatabaseConn:

    def __init__(self) -> None:
        self.__database = "Postgres"
        self._conn = "//connection_string" # PROTEGIDO - apenas a propria classe e herdeiros tem acesso
        self.user = "Lhama"

    def get_database(self) -> None:
        print(self.__database)

    def _testing_conection(self) -> None:  # PROTEGIDO - apenas a propria classe e herdeiros tem acesso
        print("Connection OK!")


class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database) # Error
        # print(self._conn)

    def select(self) -> None:
        self._testing_conection()
        print(f"connecting to {self._conn}")
        print("SELECT * FROM table")
        print(self.user)


db = DatabaseConn()
# print(db.user)

repo = Repository()
repo.select()
