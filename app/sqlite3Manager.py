import sqlite3


class SQLite3Manager:
    ...

    def __init__(self, database_name):
        self.connection = sqlite3.connect(f"{database_name}.db")
        self.cursor = self.connection.cursor()

    def action(self):
        return self.cursor

    def new_table_with_column_params(self, table_name, columns):
        try:
            buffer = "("
            for i in range(len(columns) - 1):
                buffer += f"{columns[i]},"
            buffer += f"{columns[-1]})"

        except:
            print("Exception")
            return None
        finally:
            self.action().execute(f"CREATE TABLE {table_name}{buffer}")
            self.connection.commit()

    def delete_table(self, table_name):
        try:
            self.action().execute(f"DROP TABLE {table_name}")
        except:
            return None

    def add_to_table(self, table_name, info_array, columns):
        # AGREGAR TIENE EL SIGUIENTE FORMATO:
        # info_array = ["atributo1","atributo2","atributo3",..."atributoN"]
        # columns =     ["column1","column2","colum3",..."columnN"]
        # mismo largo de columnas y atributos
        try:
            buffer1 = "("
            for i in range(len(info_array) - 1):
                buffer1 += f"'{info_array[i]}',"
            buffer1 += f"'{info_array[-1]}')"
            buffer2 = "("
            for i in range(len(columns) - 1):
                buffer2 += f"{columns[i]},"
            buffer2 += f"{columns[-1]})"
        except:
            print("Exception")
            return None
        finally:
            sentencia = f"INSERT INTO {table_name} {buffer2} VALUES {buffer1}"
            print(sentencia)
            self.action().execute(sentencia)
            self.connection.commit()

    def get_row_by_primary_key(self, table_name, primary_key, value):
        try:
            sentencia = f"SELECT * FROM {table_name} WHERE {primary_key}='{value}'"
            return list(self.action().execute(sentencia))
        except:
            return None

    def get_column(self, table_name, column):
        try:
            sentencia = f"SELECT {column} FROM {table_name}"
            return self.action().execute(sentencia)
        except:
            return None

    def row_exists(self, table_name, primary_key, value):
        return (
            len(
                list(
                    self.action().execute(
                        f"SELECT * FROM {table_name} WHERE {primary_key}='{value}'"
                    )
                )
            )
            > 0
        )

    def getAllColumns(self, table):
        sentencia = f"SELECT * FROM {table}"
        try:
            return list(self.action().execute(sentencia))
        except:
            print("La peticion a la base de datos no se pudo realizar")
            return None

    def table_exist(self, table_name):
        try:
            sentencia = f"SELECT * FROM '{table_name}' WHERE 1=0"
            self.action().execute(sentencia)
            return True
        except:
            return False


# AGREGAR TIENE EL SIGUIENTE FORMATO:
# info_array = ["atributo1","atributo2","atributo3",..."atributoN"]
# colmns =     ["column1","column2","colum3",..."columnN"]
# mismo largo de columnas y atributos


# DEBE AGREGAR, ELIMINAR Y MODIFICAR CONTAINERS
#     ENTREGAR TODA LA INFORMACIÓN EN FORMA DE LISTA PARA SER RECORRIDA O LEIDA CON FACILIDAD
#     LOS OBJETOS DEBEN SER CREADOS A PARTIR DE LA INFO DE LAS TABLAS PARA PODER SER MOSTRADOS

# camiones = [
#    "ID int","type varchar(255) NOT NULL","LOCKERS int","PRIMARY KEY (ID)"
# ]
# manager = SQLite3Manager("db")

# manager.new_table_with_column_params("", camiones)
