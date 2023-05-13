from classes import *
from sqlite3Manager import SQLite3Manager

tableCreationColumns = {
    "item_info":["name varchar(255)","locker varchar(8) NULL","description varchar(255) NULL","level int NULL","PRIMARY KEY (name)"]
    #item dentro de un camión o contenedor
}

objectColumns = {
    "truck":["name","lockers","parent_container"]
    
}

def insert_truck_from_object(manager,truck_object):
    #lista con los atributos del objeto
    atributos = [truck_object.getName(),len(truck_object.getLockerNames()),truck_object.getParentContainer()]
    #si el camión no existe (mismo nombre) se añade a la tabla truckPool para el caso de camiones
    if not manager.row_exists("truckPool", "name", truck_object.getName()):
        manager.add_to_table("truckPool", atributos, objectColumns.get("truck"))


def create_truck_from_table(manager,table_name,item_name):
    item_tuple = manager.get_row_by_primary_key(table_name, "name", item_name)[0]
    truck_name = item_tuple[0]
    truck_parent_container = item_tuple[2]
    return Truck(truck_name,truck_parent_container)

def create_truck_table(manager, truck_name,lockers):
    item_info = ["name varchar(255)","locker varchar(8) NULL","description varchar(255) NULL","level int NULL","PRIMARY KEY (name)"]
    manager.new_table_with_column_params(truck_name,item_info)
    params_truckPool = ["name","lockers","parent_container"]
    info_truckPool = [f"'{truck_name}'","1","'sala-camiones'"]
    manager.add_to_table("truckPool",info_truckPool,params_truckPool)

def insert_item_into_truck(*args,**kwargs):
    values = []
    for value in kwargs.values():
        values.append(value)
    if len(args) == 2:
        try:
            args[0].add_to_table(args[1], values, list(kwargs))
        except:
            return None
    else:
        return None
def delete_from_truck(manager,truck_table,item_name):
    try:
        manager.delete_row(truck_table,"name",item_name)
    except:
        print("No existe o el camión o el item")

def modify_item_from_truck(manager,truck_table,item_name,column_param,new_param):
    try:
        
        manager.modify_row(truck_table,"name",item_name,column_param,new_param)
    except:
        print(f"Error buscando el objeto {item_name}")

def search_items_by_name(manager,truck_table,name_value):
    l = manager.get_row_by_primary_key(truck_table,"name",name_value)
    if len(l) == 0:
        return None
    return l
    