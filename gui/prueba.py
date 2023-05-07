from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QHeaderView,
    QTableWidget,
    QCheckBox,
    QTableWidgetItem,
)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.uic import loadUi
import sys


class VentanaPrincipal(QMainWindow):
    # DESPUES PA AGREGAR NUEVOS INVENTARIOS
    invs = 3
    # DESPUES PA HACER CATEGORIAS
    ctgs = [f"Categoría {s+1}" for s in range(10)]  # EJEMPLO COMPRENDIDO
    # COLUMNAS TABLAS
    # list(columns.keys) y list(columns.values)
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

    # funcion principal de la ventana QMainWindow
    # TODO asignar mas botones a las funciones q le correspondan
    # TODO lo de agregar mas tablas
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("design.ui", self)

        # self.btn_menu.clicked.connect(self.open_menu)
        self.showPage(1, 1)

        self.btn_inv1.clicked.connect(lambda: self.showPage(1))
        self.btn_inv2.clicked.connect(lambda: self.showPage(2))
        self.btn_inv3.clicked.connect(lambda: self.showPage(3))

        self.btn_agregar.clicked.connect(lambda: self.addRow(1))

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
    def showPage(self, index: int, INIT=None):
        # primero comprueba si esta en la misma pagina y no es el showPage que inicializa
        if (self.stackedWidget.currentIndex() == index - 1) and (INIT is None):
            return
        # mueve el stackedWidget a la pagina index-1
        self.stackedWidget.setCurrentIndex(index - 1)
        # da la referencia a la tabla perteneciente a la pag del stackedWidget y hace que se pongan bonitas las columnas
        table = self.findTableRef(index)
        if table and isinstance(table, QTableWidget):
            # solo da nombre a las columnas si es que no las tiene desde un inicio
            if table.columnCount() == 0:
                table.setColumnCount(len(self.COLUMNS))
                # contexto que se debe sacar del tipo de inventario
                CONTEXT = 0
                headers = self.getColumnsValues(CONTEXT)
                # por si se cae aca (osea q alguien puso mal el contexto)
                try:
                    table.setHorizontalHeaderLabels(headers)  # type: ignore
                except:
                    raise TypeError("hay algo malo arreglalo")
            # reordena el tamaño de las columnas
            table.resizeColumnsToContents()

    # encuentra las referencias de las QTableWidgets usando su numero
    def findTableRef(self, numOfTable):
        return self.findChild(QTableWidget, f"table_inv{numOfTable}")

    # añade nuevas filas agregando un checkbox en la columna 0 de cada una
    def addRow(self, numOfTable: int):
        table = self.findTableRef(numOfTable)
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

    # nose tampoco como funciona esto
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inventario"))
        self.Inventario1.setText(_translate("MainWindow", "Inventario 1"))
        self.Inventario2.setText(_translate("MainWindow", "Inventario 2"))
        self.Inventario3.setText(_translate("MainWindow", "Inventario 3"))
        self.label_2.setText(_translate("MainWindow", "Inventario 1"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tableWidget.horizontalHeaderItem(4)

        item.setText(_translate("MainWindow", "Descripcion"))
        self.thisButton.setText(_translate("MainWindow", "ThisButton"))
        self.label_3.setText(_translate("MainWindow", "Inventario 2"))
        item = self.tableWidget1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nueva columna"))

        self.label_4.setText(_translate("MainWindow", "Inventario 3"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nueva columna"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Nueva columna"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = VentanaPrincipal()
    ui.show()
    sys.exit(app.exec_())
