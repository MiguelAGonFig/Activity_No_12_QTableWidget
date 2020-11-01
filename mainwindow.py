from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from admin_particulas import Admin_particulas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Admin_particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir_Archivo.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar_Archivo.triggered.connect(self.action_guardar_archivo)

        self.ui.Mostrar_Tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.Buscar_pushButton.clicked.connect(self.buscar_ID)

    @Slot()
    def buscar_ID(self):
        id = self.ui.Buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == str(particula.id):
                self.ui.Table.clear()
                self.ui.Table.setRowCount(1)

                ID_widget = QTableWidgetItem(str(particula.id))
                Origen_X_widget = QTableWidgetItem(str(particula.origen_x))
                Origen_Y_widget = QTableWidgetItem(str(particula.origen_y))
                Destino_X_widget = QTableWidgetItem(str(particula.destino_x))
                Destino_Y_widget = QTableWidgetItem(str(particula.destino_y))
                Velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                Red_widget = QTableWidgetItem(str(particula.red))
                Green_widget = QTableWidgetItem(str(particula.green))
                Blue_widget = QTableWidgetItem(str(particula.blue))
                Distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Table.setItem(0, 0, ID_widget)
                self.ui.Table.setItem(0, 1, Origen_X_widget)
                self.ui.Table.setItem(0, 2, Origen_Y_widget)
                self.ui.Table.setItem(0, 3, Destino_X_widget)
                self.ui.Table.setItem(0, 4, Destino_Y_widget)
                self.ui.Table.setItem(0, 5, Velocidad_widget)
                self.ui.Table.setItem(0, 6, Red_widget)
                self.ui.Table.setItem(0, 7, Green_widget)
                self.ui.Table.setItem(0, 8, Blue_widget)
                self.ui.Table.setItem(0, 9, Distancia_widget)  

                encontrado = True
                return 
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con el ID "{id}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.Table.setColumnCount(10)
        headers = ["ID", "Origen en X", "Origen en Y", "Destino en X", "Destino en Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.Table.setHorizontalHeaderLabels(headers)
        self.ui.Table.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            ID_widget = QTableWidgetItem(str(particula.id))
            Origen_X_widget = QTableWidgetItem(str(particula.origen_x))
            Origen_Y_widget = QTableWidgetItem(str(particula.origen_y))
            Destino_X_widget = QTableWidgetItem(str(particula.destino_x))
            Destino_Y_widget = QTableWidgetItem(str(particula.destino_y))
            Velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            Red_widget = QTableWidgetItem(str(particula.red))
            Green_widget = QTableWidgetItem(str(particula.green))
            Blue_widget = QTableWidgetItem(str(particula.blue))
            Distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Table.setItem(row, 0, ID_widget)
            self.ui.Table.setItem(row, 1, Origen_X_widget)
            self.ui.Table.setItem(row, 2, Origen_Y_widget)
            self.ui.Table.setItem(row, 3, Destino_X_widget)
            self.ui.Table.setItem(row, 4, Destino_Y_widget)
            self.ui.Table.setItem(row, 5, Velocidad_widget)
            self.ui.Table.setItem(row, 6, Red_widget)
            self.ui.Table.setItem(row, 7, Green_widget)
            self.ui.Table.setItem(row, 8, Blue_widget)
            self.ui.Table.setItem(row, 9, Distancia_widget)

            row +=1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self, 
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Apertura exitosa del archivo en " + ubicacion
            )
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "Fallo al intentar abir el archivo en " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Archivo creado correctamente en " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo en " + ubicacion
            )

    @Slot()
    def click_agregar_inicio(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.Salida.clear()
        self.ui.Salida.insertPlainText(str(self.particulas))