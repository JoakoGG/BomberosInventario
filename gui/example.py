from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QMessageBox

class VentanaInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Crear la tabla
        self.tabla = QTableWidget()
        self.tabla.setRowCount(5)
        self.tabla.setColumnCount(4)
        
        # Establecer los encabezados de las columnas
        self.tabla.setHorizontalHeaderLabels(['Producto', 'Cantidad', 'Precio unitario', 'Total'])
        
        # Agregar los datos a la tabla
        productos = ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4', 'Producto 5']
        cantidades = [10, 5, 3, 8, 12]
        precios_unitarios = [100, 50, 25, 75, 120]
        for i in range(len(productos)):
            # Agregar el nombre del producto a la tabla
            celda_producto = QTableWidgetItem(productos[i])
            self.tabla.setItem(i, 0, celda_producto)
            
            # Agregar la cantidad a la tabla
            celda_cantidad = QTableWidgetItem(str(cantidades[i]))
            self.tabla.setItem(i, 1, celda_cantidad)
            
            # Agregar el precio unitario a la tabla
            celda_precio_unitario = QTableWidgetItem('${:.2f}'.format(precios_unitarios[i]))
            self.tabla.setItem(i, 2, celda_precio_unitario)
            
            # Calcular y agregar el total a la tabla
            total = cantidades[i] * precios_unitarios[i]
            celda_total = QTableWidgetItem('${:.2f}'.format(total))
            self.tabla.setItem(i, 3, celda_total)
        
        # Crear los botones de modificar y eliminar
        boton_modificar = QPushButton('Modificar')
        boton_modificar.clicked.connect(self.modificar_producto)
        
        boton_eliminar = QPushButton('Eliminar')
        boton_eliminar.clicked.connect(self.eliminar_producto)
        
        # Crear un layout horizontal para los botones
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(boton_modificar)
        layout_botones.addWidget(boton_eliminar)
        
        # Crear el widget principal
        widget_principal = QWidget()
        
        # Crear un layout vertical
        layout_vertical = QVBoxLayout()
        
        # Agregar la tabla y los botones al layout
        layout_vertical.addWidget(self.tabla)
        layout_vertical.addLayout(layout_botones)
        
        # Establecer el layout en el widget principal
        widget_principal.setLayout(layout_vertical)
        
        # Establecer el widget principal como widget central de la ventana
        self.setCentralWidget(widget_principal)
    
    def modificar_producto(self):
        # Obtener la fila seleccionada
        fila_seleccionada = self.tabla.currentRow()
        
        if fila_seleccionada != -1:
            # Obtener los datos de la fila seleccionada
            nombre_producto = self.tabla.item(fila_seleccionada, 0).text()
            cantidad = self.tabla.item(fila_seleccionada, 1).text()
            precio_unitario = self.tabla.item(fila_seleccionada, 2).text()
            
            # Crear una ventana de diálogo para modificar el producto
            dialogo_modificar = DialogoModificarProducto(nombre_producto, cantidad, precio_unitario, self)
            resultado = dialogo_modificar.exec_()
            
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInventario()
    ventana.show()
    app.exec_()