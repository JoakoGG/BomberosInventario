#Todos los objetos salen de la clase container,
#tiene nombre y objetos que contiene
class Container:
    def __init__(self,name):
        self.name = name
        self.itemList = []
    
    def getName(self):
        return self.name
    def setName(self,n_name):
        self.name = n_name
    
    def getItems(self):
        return self.itemList
    def addItem(self,item):
        self.itemList.append(item)


#Container que tiene identificador y lockers (containers) disponibles
class Truck(Container):
    def __init__(self, name):
        super().__init__(name)
        self.lockers = self.itemList
        self.lockers.append(Container("Cabina"))

    def addLocker(self,locker_name):
        self.lockers.append(Container(name))

    def addLocker(self,locker_name,locker_category):
        self.lockers.append(Locker(locker_name,locker_category,self))

    def getLockerObjects(self):
        return self.lockers
    def getLockerNames(self):
        output = []
        for l in self.lockers:
            output.append(l.getName())
        return output

    def getLockerObject(self,locker_name):
        for l in self.lockers:
            if l.getName() == locker_name:
                return l
        return None

#Solo es contenido por clases Trucks, contiene los campos adicionales de categoria y
#Truck Padre 
class Locker(Container):
    def __init__(self, name, category, parent_truck):
        super().__init__(name)
        self.category = category
        self.parent_truck = parent_truck
    
    def getCategory(self):
        return self.category

    #Informacion de Truck contenedor de la clase
    def getParentTruck(self):
        return self.parent_truck
    def getParentTruckName(self):
        return self.parent_truck.getName()
    

#Falta creación de clase Item, la cual será contenida tanto por lockers como otros containers

        

        

#b = Truck("Carro 1")
#b.addLocker("Locker A","primeros auxilios")
#print(b.getLockerObject("Locker A").getName())
#print(b.getLockerObject("Locker A").getParentTruckName())
#print(b.getLockerObject("Locker A").getItems())


