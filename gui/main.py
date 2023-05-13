# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstGuiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# index [0]  -> nombre
# index [1]  -> categoria
# index [2]  -> cantidad
# index [3]  -> estado  
# index [4]  -> descripcion



class Ui_MainWindow(object):

    def addRow(self,table):
        categorias = ["Categoria 1","Categoria 2","Categoria 3","Categoria 4"]
        rowN = table.rowCount()
        table.insertRow(table.rowCount())
        btn = QtWidgets.QComboBox()
        btn.addItems(categorias)
        
        table.setCellWidget(table.rowCount()-1,1,btn)

    def createTable(self):
        _translate = QtCore.QCoreApplication.translate
        #CODIGO QUE CREA EL BOTON PARA DIRECCIONAR AL INVENTARIO
        self.newInventoryButton = QtWidgets.QPushButton(self.Inventory_Frame)
        self.newInventoryButton.setFlat(True)
        self.newInventoryButton.setObjectName("Nuevo inventario")
        self.newInventoryButton.setText(_translate("MainWindow","Inventario 4"))
        self.verticalLayout_2.addWidget(self.newInventoryButton)
        #----------------------ACA TERMINA-----------------------------------------
        #Codigo que crea una nueva pagina para la tabla de inventario
        self.new_page= QtWidgets.QWidget()
        self.new_page.setObjectName("page_4")
        #----------------------ACA TERMINA-----------------------------------------
        self.stackedWidget.addWidget(self.new_page)
        self.newLayout = QtWidgets.QVBoxLayout(self.new_page)
        self.newLayout.setObjectName("verticalLayout_6")
        #Creacion del QFRAME
        self.newFrame = QtWidgets.QFrame(self.new_page)
        self.newFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newFrame.setObjectName("frame_7")
        #----------------------ACA TERMINA-----------------------------------------    
        
        self.inLayout = QtWidgets.QVBoxLayout(self.newFrame)
        self.inLayout.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.newFrame)
        self.label_2.setObjectName("label_2")
        self.inLayout.addWidget(self.label_2)

        self.newtableWidget = QtWidgets.QTableWidget(self.newFrame)
        self.newtableWidget.setObjectName("table")
        self.newtableWidget.setColumnCount(5)
        self.newtableWidget.setRowCount(5)

        self.newInventoryButton.clicked.connect(lambda : (self.stackedWidget.setCurrentIndex(3)))
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Inventory_Frame = QtWidgets.QFrame(self.frame)
        self.Inventory_Frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(42,53,66);\n"
"    color: white;\n"
"    font: 25 11pt \"Microsoft JhengHei Light\";\n"
"}\n"
"QPushButton{\n"
"    background-color : rgb(42,53,66);\n"
"    color: white;\n"
"    font: 25 11pt \"Microsoft JhengHei Light\";\n"
"}\n"
"")
        self.Inventory_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Inventory_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Inventory_Frame.setLineWidth(0)
        self.Inventory_Frame.setObjectName("Inventory_Frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Inventory_Frame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(-1, 13, -1, 2)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.Inventory_Frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(38, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.Inventario1 = QtWidgets.QPushButton(self.Inventory_Frame)
        self.Inventario1.setFlat(True)
        self.Inventario1.setObjectName("Inventario1")
        self.verticalLayout_2.addWidget(self.Inventario1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Inventario2 = QtWidgets.QPushButton(self.Inventory_Frame)
        self.Inventario2.setFlat(True)
        self.Inventario2.setObjectName("Inventario2")
        self.verticalLayout_2.addWidget(self.Inventario2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.Inventario3 = QtWidgets.QPushButton(self.Inventory_Frame)
        self.Inventario3.setFlat(True)
        self.Inventario3.setObjectName("Inventario3")
        self.verticalLayout_2.addWidget(self.Inventario3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.Inventory_Frame)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color : rgb(42,53,66);\n"
"}\n"
"QPushButton{\n"
"    background-color : rgb(42,53,66);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Open_Button = QtWidgets.QPushButton(self.frame_4)
        self.Open_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/588a64e0d06f6719692a2d10.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Open_Button.setIcon(icon)
        self.Open_Button.setFlat(True)
        self.Open_Button.setObjectName("Open_Button")
        self.horizontalLayout_4.addWidget(self.Open_Button)
        spacerItem4 = QtWidgets.QSpacerItem(886, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.inventory = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("CMU Bright")
        self.inventory.setFont(font)
        self.inventory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inventory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inventory.setLineWidth(0)
        self.inventory.setObjectName("inventory")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inventory)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.inventory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(700, 100))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.page_1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.verticalLayout_7.addWidget(self.tableWidget)
        self.thisButton = QtWidgets.QPushButton(self.frame_3)
        self.thisButton.setObjectName("thisButton")
        self.verticalLayout_7.addWidget(self.thisButton)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.page_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableWidget1 = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget1)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.page_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.verticalLayout_10.addWidget(self.tableWidget_2)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.inventory)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.verticalLayout_9.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        #Funciones para cambiar de pagina index (0,1,2)
        self.Inventario1.clicked.connect(lambda : (self.stackedWidget.setCurrentIndex(0)))
        self.Inventario2.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(1)))
        self.Inventario3.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(2)))

        self.thisButton.clicked.connect(lambda: (self.addRow(self.tableWidget)))
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.createTable()

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())