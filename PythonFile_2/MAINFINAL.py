from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalTableModel
import sys
from TableClass import TableModel
from sqlite3Manager import SQLite3Manager
class VentanaPrincipal(QMainWindow):
    columns = ["Nombre","Categoria","Cantidad"]
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        loadUi(r"C:\Users\danie\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\qt5_applications\Qt\bin\FirstGuiDesign2.ui", self)
    
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.table1.setDragDropOverwriteMode(False)
        
        # Seleccionar toda la fila
        self.table1.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.table1.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.table1.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.table1.setWordWrap(False)
        # Alineación del texto del encabezado
        self.table1.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
          # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.table1.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.table1.horizontalHeader().setStretchLastSection(True)
        #MODIFICACIONES A LA TABLA 1
        self.stackedWidget.setCurrentIndex(1)
        #Creamos un modelo visual para el QTableView
        self.actualizarTabla(self.table2,'inventario')
        # Asignamos la funcion agregarRegistro al boton de agregar
        self.Agregar2.clicked.connect(lambda:(self.agregarRegistro(self.table2,'inventario')))
        # Asignamos la funcion eliminar a la tabla
        self.lineEdit2.textChanged.connect(self.proxyModel.setFilterFixedString)


        

        self.eliminar.clicked.connect(self._removeRow)
        # Asignamos la funcion agregar a la tabla (necesita la tabla)
        self.agregar.clicked.connect(lambda: (self.addRow(self.table1)))
        #Asignamos funciones a la lineEdit para buscar
        self.lineEditT1.setPlaceholderText("Buscar...")
        self.lineEditT1.textChanged.connect(lambda: (self.buscar(self.table1,self.lineEditT1)))
    
    
    def actualizarTabla(self,tabla,tablaBD):
        #Primero llamamos a la base de datos 
        db = SQLite3Manager('database')
        #Despues creamos el modelo de la tabla
        datos = db.getAllColumns(tablaBD)
        #Ingresamos los datos como matriz [numeroColumnas][datosXColumna]
        
        modelo = TableModel(datos)
        #Creamos un modelo proxy para poder realizar busquedas
        self.proxyModel = QSortFilterProxyModel()
        #Le decimos al modelo que debe buscar en toda la tabla
        self.proxyModel.setFilterKeyColumn(-1)
        #Se debe basar en el modelo de la base
        self.proxyModel.setSourceModel(modelo)
       
        tabla.setModel(self.proxyModel)
        return modelo

    def _removeRow(self):
        filaSeleccionada = self.table1.selectedItems()

        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            self.table1.removeRow(fila)

            self.table1.clearSelection()
        else:
            QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                 QMessageBox.Ok)

    def agregarRegistro(self,tabla,tablaBD):
        #Funcion formulario
        array = []
        db = SQLite3Manager(tablaBD)
        db.add_to_table('inventario',array,self.columns)
        self.actualizarTabla(tabla,tablaBD)

        
        
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = VentanaPrincipal()
    ui.show()
    sys.exit(app.exec_())
