import modules as m
from classes import *
from sqlite3Manager import SQLite3Manager

c = SQLite3Manager("database")
m.insertTruckFromObject(c,Truck("camion1","sala-camiones"))















