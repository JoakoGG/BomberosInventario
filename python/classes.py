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


#Visualizar informacion de Items dentro de Locker 
    def getItemObject(self,item_name):
        for l in self.itemList:
            if l.getName() == item_name:
                return l
        return None
    def getItemName(self,item_name):
        for l in self.itemList:
            if l.getName() == item_name:
                return l.getName()
        return None

#Añadir Items al Locker mediante parámetros, método heredado
#de getItem() agrega cualquier otro tipo de objeto, incluso camiones
    def createAndAddItem(self,name,description,level):
        i = Item(str(name),str(description),self,int(level))
        self.addItem(i)

    

#Clase Item, es contenida por Locker, proximamente por cualquier otro Container
class Item(Container):
    def __init__(self, name, description, parent_container,level):
        super().__init__(name)
        self.description = description
        self.parent_locker = parent_container
        self.level = level
        self.is_operative = True


#Getters y Setters predeterminados
    def getDescription(self):
        return self.description
    def setDescription(self,n_description):
        self.description = n_description

    def getParentContainer(self):
        return self.parent_locker
    def getParentContainerName(self):
        return self.parent_locker.getName()

    def getLevel(self):
        return self.level
    def setLevel(self,n_level):
        if not n_level.isDigit():
            return None
        self.level = n_level

    def getInfoFormated(self):
        return "Item [Name:"+str(self.getName())+", Description: "+str(self.getDescription())+", Level: "+str(self.getLevel())+"]"

    
        

        

#b = Truck("Carro 1")
#b.addLocker("Locker A","primeros auxilios")
#b.getLockerObject("Locker A").createAndAddItem("oxigeno","tanque de oxigeno",3)



