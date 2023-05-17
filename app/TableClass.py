from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TableModel(QAbstractTableModel):
    header = {
        "id": "ID",
        "objid": "Código",
        "name": "Nombre",
        "subinv": "Cajonera",
        "level": "Nivel",
        "state": "Estado",
        "obs": "Observación",
        "brand": "Marca",
        "model": "Modelo",
        "desc": "Descripción",
    }
    header_labels = list(header.values())

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def setData(self, new_data):
        self._data = new_data

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    # Traceback (most recent call last):
    # File "c:\Users\Tomas\OneDrive\Desktop\pruebas\TableClass.py", line 46, in columnCount
    # TODO return len(self._data[0])
    #                 ~~~~~~~~~~^^^
    # IndexError: list index out of range
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
