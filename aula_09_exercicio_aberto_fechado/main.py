from repositorio import Repositorio
from databases import PostgresBD, MySqlBD

db_conn_postgres = PostgresBD()
db_conn_mysql = MySqlBD()
repo = Repositorio()

repo.insert(db_conn_postgres)
print()
repo.insert(db_conn_mysql)

