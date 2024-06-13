from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QSpacerItem, QSizePolicy, QScrollArea
from TaskingComponents.Logic import MyLogic

class TaskingApp(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        #self.setFixedSize(700, 380)
        self.my_logic = MyLogic(self)

        self.layout = QGridLayout()

        # ======================= Add Button =======================
        self.add_button = QPushButton('Añadir QTextEdit')
        self.add_button.clicked.connect(self.my_logic.add_text_edit)
        self.layout.addWidget(self.add_button, 0, 0, 1, 1)

        # ======================= Add ScrollArea =======================
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Permitir que el widget interno se ajuste al área de desplazamiento
        self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:0, y2:0.5,
                stop:0 rgba(22, 22, 22, 255), stop:0 rgba(18, 18, 18, 255));
                border: none;
            }
        """)

        # Crear un QWidget que contendrá los QTextEdit y su layout
        self.text_edit_container = QWidget()
        self.text_edit_container.setStyleSheet("background:transparent;")
        self.text_edit_layout = QVBoxLayout(self.text_edit_container)
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.text_edit_layout.addItem(self.spacer)

        self.scroll_area.setWidget(self.text_edit_container)

        # Añadir la scroll area al layout principal
        self.layout.addWidget(self.scroll_area, 1, 0, 1, 1) 
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 10)
        self.layout.setColumnStretch(0, 1)

        # ======================= Main Layout =======================
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.layout)

        if MainWindow.j == 1:
            self.my_logic.loadData()