from classes import *
from sqlite3Manager import SQLite3Manager

tableCreationColumns = {
    "truck":["name varchar(255)","lockers int","parent_container","PRIMARY KEY (name)"]
}

objectColumns = {
    "truck":["name","lockers","parent_container"]
    
}

def insertTruckFromObject(manager,truck_object):
    #lista con los atributos del objeto
    atributos = [truck_object.getName(),len(truck_object.getLockerNames()),truck_object.getParentContainer()]
    #si el camión no existe (mismo nombre) se añade a la tabla truckPool para el caso de camiones
    if not manager.row_exists("truckPool", "name", truck_object.getName()):
        manager.add_to_table("truckPool", atributos, objectColumns.get("truck"))


def createTruckFromTable(manager,table_name,item_name):
    item_tuple = manager.get_row_by_primary_key(table_name, "name", item_name)[0]
    truck_name = item_tuple[0]
    truck_parent_container = item_tuple[2]
    return Truck(truck_name,truck_parent_container)