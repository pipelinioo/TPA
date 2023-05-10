from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QWidget


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1 seccion Practica Prueba individual")
        self.resize(600, 400)

        # #crear la seccion superior de la ventana
        self.username_label = QLabel("NOMBRE USUARIO")
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setCentralWidget(self.username_label)

        # ##caja central con imagen y tabla
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("ruta_de_la_imagen.jpg").scaledToHeight(150))
        self.description_label = QLabel("Descripción de la imagen")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Atributo", "Valor"])
        self.table_widget.setItem(0, 0, QTableWidgetItem("Atributo 1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Valor 1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Atributo 2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Valor 2"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("Atributo 3"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("Valor 3"))
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.image_label)
        central_layout.addWidget(self.description_label)
        central_layout.addWidget(self.table_widget)
        central_group_box = QGroupBox()
        central_group_box.setLayout(central_layout)

        ## boton ok
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.close)
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.ok_button)
        bottom_layout.addStretch()
        bottom_widget = QWidget()
        bottom_widget.setLayout(bottom_layout)

        ### agregar a la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(central_group_box)
        main_layout.addWidget(bottom_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()
