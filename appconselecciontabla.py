from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from TableClass import TableModel
from sqlite3Manager import SQLite3Manager
#Es necesario el import path para que el programa pueda funcionar sin problemas en cualquier PC
from pathlib import Path

import sys

#---
class Leyenda(QWidget):
    def __init__(self):
        super().__init__()
        #Busca la dirección absoluta del diseño
        path = str(Path.cwd() / "app/leyenda.ui")
        #Hace que la dirección sea compatible con las funciones de pyqt5 (cambia '\' por '/')
        winpath = path.replace("\\","/")
        loadUi(winpath, self)
        self.setWindowTitle("Leyenda")
#---

class VentanaPrincipal(QMainWindow):
    # COLUMNAS TABLAS
    # list(columns.keys()) y list(columns.values())

    COLUMNS = {
        "id": "ID",
        "objid": "Código",
        "name": "Nombre",
        "subinv": ["Cajonera", "Estante"],
        "level": "Nivel",
        "state": "Estado",
        "obs": "Observación",
        "brand": "Marca",
        "model": "Modelo",
        "desc": "Descripción",
    }
    ADDCOLUMNS = [
        "objid",
        "name",
        "subinv",
        "level",
        "state",
        "obs",
        "brand",
        "model",
        "desc",
    ]
    DBCOLUMNS = [
        "id INTEGER PRIMARY KEY autoincrement",
        "objid int NULL",  # por ahora null
        "name varchar(255)",
        "subinv varchar(255)",
        "level int",
        "state varchar(255)",
        "obs varchar(255) NULL",
        "brand varchar(255) NULL",
        "model varchar(255) NULL",
        "desc varchar(255) NULL",
    ]
    
    db = SQLite3Manager("database")
    inv = 0

    # funcion principal de la ventana QMainWindow
    # TODO asignar mas botones a las funciones q le correspondan
    # TODO lo de agregar mas tablas
    #.---.
    def abrirLeyenda(self, checked):
        self.w = Leyenda()
        self.w.show()

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            print("X: {0} | Y: {1}".format(ix.column(), ix.row()))
    #.---.

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        #Busca la dirección absoluta del diseño
        path = str(Path.cwd() / "app/design.ui")
        #Hace que la dirección sea compatible con las funciones de pyqt5 (cambia '\' por '/')
        winpath = path.replace("\\","/")
        loadUi(winpath, self)

        # self.btn_menu.clicked.connect(self.open_menu)
        self.showPage(1, 1, 1)

        #.---.
        self.btn_leyenda.clicked.connect(self.abrirLeyenda)

        self.table_inv.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        #.---.

        # Funcion buscar
        self.le_buscar.setPlaceholderText("Buscar...")
        self.proxyModel.setFilterCaseSensitivity(0)
        self.le_buscar.textChanged.connect(self.proxyModel.setFilterFixedString)

        # Botones inventarios
        self.btn_inv1.clicked.connect(lambda: self.showPage(1, 1))
        self.btn_inv2.clicked.connect(lambda: self.showPage(1, 2))
        self.btn_inv3.clicked.connect(lambda: self.showPage(1, 3))
        # self.btn_inv3.clicked.connect(lambda: self.db.delete_table("inventario1"))

        self.db.delete_table("inventarioNone")

        self.btn_agregar.clicked.connect(lambda: self.showPage(2))

        self.btn_addnew.clicked.connect(lambda: self.addregister())

    # para obtener dependiendo del contexto una lista de las columnas con "Cajonera" o "Estante"
    # TODO hacer para q se pueda identificar el contexto del inventario al que se le asigna
    def getColumnsValues(self, op: int) -> list[str] | None:
        # Comprobar que es 0 o 1
        if op > 1 or op < 0:
            return None

        # Obtener todos los VALUES de COLUMNS como una lista
        arr = list(self.COLUMNS.values())
        # Modificar el "subinv" dependiendo del contexto
        arr[list(self.COLUMNS.keys()).index("subinv")] = self.COLUMNS["subinv"][op]

        return arr

    # usa index-1 para q los indices siempre coincidan con los nombres de los objetos
    def showPage(self, index: int, table=None, INIT=None):
        # primero comprueba si esta en la misma pagina y no es el showPage que inicializa
        if (
            (self.stackedWidget.currentIndex() == index - 1)
            and (INIT is None)
            and (table == self.inv)
        ):
            return
        # mueve el stackedWidget a la pagina index-1
        self.stackedWidget.setCurrentIndex(index - 1)

        if table != None:
            tablename = f"inventario{table}"
            self.inv = table
            print(tablename)
            # self.lb_title. CAMBIAR TEXTO TITULO

            # datos = db.getAllColumns(f"inventario{table}")
            if not self.db.table_exist(tablename):
                columns = self.DBCOLUMNS
                self.db.new_table_with_column_params(tablename, columns)

            datos = self.db.getAllColumns(f"{tablename}")

            if datos == None:
                print("NO existe tabla")
                return None
            try:
                modelo = TableModel(datos)
            except:
                print("error al tener modelo")
            finally:
                # Se crea un modelo y se le asigna al QTableView
                self.proxyModel = QSortFilterProxyModel()
                self.proxyModel.setFilterKeyColumn(-1)  # Busqueda en todas las columnas
                self.proxyModel.setSourceModel(modelo)
                self.table_inv.setModel(self.proxyModel)

    # INVESTIGAR hacer formulario en un popup
    def addregister(self):
        # TODO HACER OBLIGATORIO EL FORMULARIO

        name = self.le_name.text()
        state = self.cb_state.currentText()
        subinv = self.cb_subinv.currentText()
        level = self.cb_level.currentText()
        obs = self.te_obs.toPlainText()
        brand = self.le_brand.text()
        model = self.le_model.text()
        desc = self.te_desc.toPlainText()

        objid = 0  # funcion
        array = [objid, name, subinv, level, state, obs, brand, model, desc]
        print(array)

        self.db.add_to_table(f"inventario{self.inv}", array, self.ADDCOLUMNS)
        self.cleanregister()
        self.showPage(1, self.inv)

    def cleanregister(self):
        self.le_name.setText("")
        self.cb_state.setCurrentIndex(0)
        self.cb_subinv.setCurrentIndex(0)
        self.cb_level.setCurrentIndex(0)
        self.te_obs.setText("")
        self.le_brand.setText("")
        self.le_model.setText("")
        self.te_desc.setText("")

    def addRow(self):
        table = self.findTableRef()
        if table and isinstance(table, QTableWidget):
            table.insertRow(table.rowCount())
            table.setCellWidget(table.rowCount() - 1, 0, QCheckBox())

    # esto no lo toque pa na no se que hace
    def createTable(self):
        _translate = QtCore.QCoreApplication.translate
        # CODIGO QUE CREA EL BOTON PARA DIRECCIONAR AL INVENTARIO
        self.newInventoryButton = QtWidgets.QPushButton(self.Inventory_Frame)
        self.newInventoryButton.setFlat(True)
        self.newInventoryButton.setObjectName("Nuevo inventario")
        self.newInventoryButton.setText(_translate("MainWindow", "Inventario 4"))
        self.verticalLayout_2.addWidget(self.newInventoryButton)
        # ----------------------ACA TERMINA-----------------------------------------
        # Codigo que crea una nueva pagina para la tabla de inventario
        self.new_page = QtWidgets.QWidget()
        self.new_page.setObjectName("page_4")
        # ----------------------ACA TERMINA-----------------------------------------
        self.stackedWidget.addWidget(self.new_page)
        self.newLayout = QtWidgets.QVBoxLayout(self.new_page)
        self.newLayout.setObjectName("verticalLayout_6")
        # Creacion del QFRAME
        self.newFrame = QtWidgets.QFrame(self.new_page)
        self.newFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newFrame.setObjectName("frame_7")
        # ----------------------ACA TERMINA-----------------------------------------

        self.inLayout = QtWidgets.QVBoxLayout(self.newFrame)
        self.inLayout.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.newFrame)
        self.label_2.setObjectName("label_2")
        self.inLayout.addWidget(self.label_2)

        self.newtableWidget = QtWidgets.QTableWidget(self.newFrame)
        self.newtableWidget.setObjectName("table")
        self.newtableWidget.setColumnCount(5)
        self.newtableWidget.setRowCount(5)

        self.newInventoryButton.clicked.connect(
            lambda: (self.stackedWidget.setCurrentIndex(3))
        )
        item = QtWidgets.QTableWidgetItem()
        self.newtableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.newtableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.newtableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.newtableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.newtableWidget.setVerticalHeaderItem(4, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = VentanaPrincipal()
    ui.show()
    sys.exit(app.exec_())
