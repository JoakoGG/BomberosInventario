import sqlite3

class SQLite3Manager():
    ...
    def __init__(self,database_name):
        self.connection = sqlite3.connect(f"../{database_name}.db")
        self.cursor = self.connection.cursor()

    def action(self):
        return self.cursor

    def new_table(self,table_name):
        self.action().execute(f"CREATE TABLE {table_name}")
        self.connection.commit()

    def new_table_with_column_params(self,table_name,columns):
        try:
            buffer = "("
            for i in range(len(columns)-1):
                buffer+=f'{columns[i]},'
            buffer+= f'{columns[-1]})'
            
        except:
            print("Exception")
            return None
        finally:
            self.action().execute(f"CREATE TABLE {table_name}{buffer}")
            self.connection.commit()
    
    def delete_table(self,table_name):
        try:
            self.action().execute(f"DROP TABLE {table_name}")
        except:
            return None
        
    



    #DEBE AGREGAR, ELIMINAR Y MODIFICAR CONTAINERS
    #     ENTREGAR TODA LA INFORMACIÓN EN FORMA DE LISTA PARA SER RECORRIDA O LEIDA CON FACILIDAD
    #     LOS OBJETOS DEBEN SER CREADOS A PARTIR DE LA INFO DE LAS TABLAS PARA PODER SER MOSTRADOS

#camiones = [
#    "ID int","type varchar(255) NOT NULL","LOCKERS int","PRIMARY KEY (ID)"
#]
#manager = SQLite3Manager("TABLEPRUEBAS")

#manager.new_table_with_colum_params("", camiones)