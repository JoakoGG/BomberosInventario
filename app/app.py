import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from TableClass import TableModel
from sqlite3Manager import SQLite3Manager

import sys

INVENTORY = "inventory"


class Leyenda(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("leyenda.ui", self)
        self.setWindowTitle("Leyenda")


class VentanaPrincipal(QMainWindow):
    # COLUMNAS TABLAS
    # list(columns.keys()) y list(columns.values())
    COLUMNS = {
        "id": "ID",
        "name": "Nombre",
        "inv": "Inventario",
        "subinv": ["Cajonera", "Estante"],
        "level": "Nivel",
        "state": "Estado",
        "obs": "Observación",
        "desc": "Descripción",
        "qty": "Cantidad",
    }
    # Arreglo para hacer query a la BD
    ADDCOLUMNS = [
        "name",
        "inv",
        "subinv",
        "level",
        "state",
        "obs",
        "desc",
        "qty",
    ]
    # Arreglo para crear la BD
    DBCOLUMNS = [
        "id INTEGER PRIMARY KEY autoincrement",
        "name varchar(255)",
        "inv varchar(255)",  # INVENTARIO EN DONDE ESTA (bodega, camionX)
        "subinv varchar(255)",  # Cajonera/Estante
        "level int",  # Nivel dentro del subinventario
        "state varchar(255)",  # Estados QUE DEFINAN ELLOS (agregar => operativo, dadodebaja, perdido, prestado)
        "obs varchar(255) NULL",  # Observación
        "desc varchar(255) NULL",  # descripcion
        "qty int",  # cantidad
    ]
    db = SQLite3Manager("database")
    setInv = -1
    inventories = [
        "Bodega",
        "Camion 1",
        "Camion 2",
        "Camion 3",
    ]
    FILTERS = {
        "Sin Filtro": -1,
        "ID": 0,
        "Nombre": 1,
        "Inventario": 2,
        "Cajonera": 3,
        "Nivel": 4,
        "Estado": 5,
        "Observación": 6,
        "Descripción": 7,
        "Cantidad": 8,
    }
    SUBINVS = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "Techo": 7,
    }
    STATES = {
        "Sin uso": 0,
        "Operativo": 1,
        "Dado de baja": 2,
        "Perdido": 3,
        "Prestado": 4,
    }
    LEVELS = {
        "Superior": 0,
        "Medio": 1,
        "Inferior": 2,
    }
    bufferdata = None

    # funcion principal de la ventana QMainWindow
    # TODO asignar mas botones a las funciones q le correspondan
    # TODO lo de agregar mas tablas
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("design.ui", self)

        btn_inv1: QPushButton
        btn_inv2: QPushButton
        btn_inv3: QPushButton
        btn_agregar: QPushButton
        btn_addnew: QPushButton
        btn_menu: QPushButton
        btn_canceladdnew: QPushButton
        btn_deselect: QPushButton
        le_buscar: QLineEdit
        proxyModel: QSortFilterProxyModel
        cb_filtros: QComboBox
        tv: QTableView = self.table_inv

        # crear db si no hay una
        if not self.db.table_exist(INVENTORY):
            self.db.new_table_with_column_params(INVENTORY, self.DBCOLUMNS)

        # proxymodel para la busqueda
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setFilterKeyColumn(-1)  # Busqueda en todas las columnas

        # self.btn_menu.clicked.connect(self.open_menu)
        self.showPage(1, 1)

        # Funcion buscar
        self.le_buscar.setPlaceholderText("Buscar...")
        self.proxyModel.setFilterCaseSensitivity(0)
        self.le_buscar.textChanged.connect(self.proxyModel.setFilterFixedString)

        # TODO AUTOMATIZAR ESTO
        bi1: QPushButton = self.btn_inv1
        bi2: QPushButton = self.btn_inv2
        bi3: QPushButton = self.btn_inv3
        bi4: QPushButton = self.btn_inv4
        bi1.setText(self.inventories[0])
        bi2.setText(self.inventories[1])
        bi3.setText(self.inventories[2])
        bi4.setText(self.inventories[3])

        # Botones inventarios
        bi1.clicked.connect(lambda: self.showPage(1, 1))
        bi2.clicked.connect(lambda: self.showPage(1, 2))
        bi3.clicked.connect(lambda: self.showPage(1, 3))
        bi4.clicked.connect(lambda: self.showPage(1, 4))
        # self.btn_inv3.clicked.connect(lambda: self.db.delete_table("inventario1"))
        # self.db.delete_table("inventarioNone")
        self.btn_agregar.clicked.connect(lambda: self.showPage(2))
        self.btn_addnew.clicked.connect(lambda: self.addregister())
        self.btn_menu.clicked.connect(lambda: self.showSideBar())
        self.btn_canceladdnew.clicked.connect(lambda: self.showPage(1, self.setInv))

        self.btn_editar.clicked.connect(lambda: self.showPage(3))
        self.btn_canceledit.clicked.connect(lambda: self.showPage(1, self.setInv))
        self.btn_saveedit.clicked.connect(lambda: self.saveRegister())

        self.btn_eliminar.clicked.connect(lambda: self.deleteRegister())

        self.btn_deselect.clicked.connect(lambda: self.deselectCB(self.cb_filtros))
        self.setFilters(self.cb_filtros)
        print(self.cb_filtros.currentIndex())
        self.cb_filtros.currentTextChanged.connect(
            lambda: self.setFilter(self.cb_filtros.currentText())
        )

        # TODO
        self.btn_leyenda.clicked.connect(self.abrirLeyenda)
        self.table_inv.doubleClicked.connect(self.doubleClick)

        tv.installEventFilter(self)
        tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        # self.table_inv.ContextMenu.clicked(lambda: self.menu())
        # self.table_inv.doubleClicked.connect(self.edit)

    def abrirLeyenda(self, checked):
        self.w = Leyenda()
        self.w.show()

    def doubleClick(self, index):
        print("Fila: {0} | Columna: {1}".format(index.row(), index.column()))
        if index.column() == 5:
            indiceId = self.table_inv.model().index(index.row(), 0).data()
            # print(self.tablename)
            fila = self.db.get_rows_by_column_field(INVENTORY, "id", str(indiceId))
            print(fila)
            print(indiceId)
            print(self.table_inv.model().data(index))
            # print(self.table_inv.currentIndex().row())

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.table_inv:
            self.contextMenu(event)
            return True
        else:
            return super().eventFilter(source, event)

    def contextMenu(self, event):
        menu: QMenu = QMenu(self)

        opcionesInventarios: QMenu = QMenu("Mover elementos hacia...")
        for inv in self.inventories:
            qA = QAction(f"{inv}", opcionesInventarios)
            qA.triggered.connect(lambda: self.moverHaciaContenedor(event, inv=inv))
            opcionesInventarios.addAction(qA)

        deleteData = QAction("Eliminar elementos", self)
        deleteData.triggered.connect(lambda: self.deleteRegister())
        changeDataState = QAction("Asignar nuevo estado", self)
        changeDataState.triggered.connect(lambda: NotImplemented)
        # TODO e implementar más funciones

        menu.addMenu(opcionesInventarios)
        menu.addAction(deleteData)
        menu.addAction(changeDataState)
        # menu.addMenu(secmenu)
        # menu.popup(QCursor.pos())
        menu.exec_(event.globalPos())

    # def eventFilter(self, source, event):
    #     if event.type() == QEvent.ContextMenu and source is self.table_inv:
    #         self.menu(event.globalPos())
    #         print((event.globalPos()))
    #         return True
    #     else:
    #         return super().eventFilter(source, event)

    # HACER FUNCION DE EDITAR CON LA COSA DEL PANTOJA O LO Q SEA DE LA BASE DE DATOS
    def moverHaciaContenedor(self, event, inv=None):
        rows: list = self.getSelectedRows(event)
        # self.view = Leyenda()
        # self.view.show()
        # print(inv)

    def editarFila(self):
        ...

    def getSelectedRows(self) -> list:
        tv: QTableView = self.table_inv
        # ENTREGA LOS INDICES DE LAS FILAS SELECCIONADAS
        rows = {index.row() for index in tv.selectionModel().selectedIndexes()}
        # print(f"Filas seleccionadas: {rows}")
        output = []
        for row in rows:
            rowdata = []
            for column in range(tv.model().columnCount()):
                index = tv.model().index(row, column)
                rowdata.append(index.data())
            output.append(rowdata)
        # ENTREGA UN ARREGLO DE ARREGLOS CON LOS DATOS DE LAS FILAS SELECCIONADAS
        return output
        # fila = tv.rowAt(event.pos().y())
        # columna = tv.columnAt(event.pos().x())
        # print((fila, columna))

    def setFilter(self, filter):
        n = self.FILTERS.get(filter)
        self.proxyModel.setFilterKeyColumn(n)

    def setTableData(self, invnumber):
        datos = self.db.get_rows_by_column_field(
            INVENTORY, "inv", self.inventories[invnumber - 1]
        )
        try:
            if datos == None:
                print("No existe la tabla")
            modelo = TableModel(datos)
        except:
            print("Error al obtener la informacion de la base de datos")
        finally:
            # Se crea un modelo y se le asigna al QTableView
            self.proxyModel.setSourceModel(modelo)
            self.table_inv.setModel(self.proxyModel)

    def setFilters(self, combobox):
        combobox.addItems(["Sin Filtro"] + self.getColumnsValues(0))

    def deselectCB(self, combobox):
        combobox.setCurrentIndex(0)

    def showSideBar(self):
        if not self.frameinv.isHidden():
            self.frameinv.hide()
        else:
            self.frameinv.show()

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
    def showPage(self, index, table=None):
        sidemenu = self.frameinv
        # # primero comprueba si esta en la misma pagina y no es el showPage que inicializa
        # if (
        #     (self.stackedWidget.currentIndex() == index - 1)
        #     and (INIT is None)
        #     and (table == self.setInv)
        # ):
        #     return
        # mueve el stackedWidget a la pagina index-1

        match index:
            case 1:
                self.setInv = table
                title = str(self.inventories[table - 1])
                self.lb_title.setText(title)
                sidemenu.show()
                self.setTableData(table)
            case 2:
                sidemenu.hide()
                ...
            case 3:
                if len(self.selectRow()) != 1:
                    alert = QMessageBox(self)
                    alert.setWindowTitle("Advertencia")
                    alert.setText("Por favor, escoja solo una fila.")
                    alert.show()
                    return
                sidemenu.hide()
                try:
                    self.setData(self.selectRow()[0])
                except:
                    ...
                ...
            case 4:
                ...

        self.stackedWidget.setCurrentIndex(index - 1)

    def selectRow(self):
        return self.getSelectedRows()

    def setData(self, data):
        print(f"los datos son:\n {data}")
        self.le_nameEDIT.setText(data[1])
        self.cb_stateEDIT.setCurrentIndex(self.STATES.get(data[5]))
        self.cb_subinvEDIT.setCurrentIndex(self.SUBINVS.get(data[3]))
        self.cb_levelEDIT.setCurrentIndex(self.LEVELS.get(data[4]))
        self.sp_qtyEDIT.setValue(data[8])
        self.te_obsEDIT.setText(data[6])
        self.te_descEDIT.setText(data[7])

        self.bufferdata = data.pop(0)
        print(self.bufferdata)
        ...

    def saveRegister(self):
        name = self.le_nameEDIT.text()
        state = self.cb_stateEDIT.currentText()
        inv = self.inventories[self.setInv - 1]
        subinv = self.cb_subinvEDIT.currentText()
        level = self.cb_levelEDIT.currentText()
        qty = self.sp_qtyEDIT.value()
        obs = self.te_obsEDIT.toPlainText()
        desc = self.te_descEDIT.toPlainText()
        array = [name, inv, subinv, level, state, obs, desc, qty]
        # print(f"se va a guardar:\n {array}")
        self.db.edit_row(INVENTORY, self.ADDCOLUMNS, array, "id", self.bufferdata)
        self.showPage(1, self.setInv)

    # INVESTIGAR hacer formulario en un popup
    def addregister(self):
        # TODO HACER OBLIGATORIO EL FORMULARIO

        name = self.le_name.text()
        state = self.cb_state.currentText()
        inv = self.inventories[self.setInv - 1]
        subinv = self.cb_subinv.currentText()
        level = self.cb_level.currentText()
        qty = self.sp_qty.value()
        obs = self.te_obs.toPlainText()
        desc = self.te_desc.toPlainText()

        array = [name, inv, subinv, level, state, obs, desc, qty]
        # print(array)

        self.db.add_to_table(INVENTORY, array, self.ADDCOLUMNS)
        self.cleanregister()
        self.showPage(1, self.setInv)

    def cleanregister(self):
        self.le_name.setText("")
        self.cb_state.setCurrentIndex(0)
        self.cb_subinv.setCurrentIndex(0)
        self.cb_level.setCurrentIndex(0)
        self.sp_qty.setValue(0)
        self.te_obs.setText("")
        self.te_desc.setText("")

    def addRow(self):
        table = self.findTableRef()
        if table and isinstance(table, QTableWidget):
            table.insertRow(table.rowCount())
            table.setCellWidget(table.rowCount() - 1, 0, QCheckBox())

    def editRegister(self):
        model = self.table_inv.model()
        row = 1
        data = []
        for column in range(len(self.FILTERS)):
            index = model.index(row, column)
            info = str(model.data(index))
            data.append(info)

    def deleteRegister(self):
        model = self.table_inv.model()
        selectionMode = self.table_inv.selectionModel()
        if selectionMode.hasSelection():
            index_selected = selectionMode.selectedIndexes()
            row_selected = list(set(index.row() for index in index_selected))
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Question)
            message_box.setWindowTitle("Eliminacion de filas")
            message_box.setText(f"¿Desea eliminar {len(row_selected)} filas(s)")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = message_box.exec_()
            if result == QMessageBox.Yes:
                row_selected.sort(reverse=True)
                for row in row_selected:
                    model.removeRow(row)
                    id = str(model.data(model.index(row, 0)))
                    self.db.delete_row(INVENTORY, "id", id)
                    print(row)
            self.setTableData(self.setInv)
        else:
            # Si no hay selección, mostrar un mensaje de advertencia
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Eliminar fila")
            message_box.setText("No se ha seleccionado ninguna fila.")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()

    def getInfoRow(self, row):
        array = []
        model = self.table_inv.model()
        for column in range(len(self.FILTERS)):
            index = model.index(row, column)
            info = str(model.data(index))
            array.append(info)
            print(info)
        return array

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
