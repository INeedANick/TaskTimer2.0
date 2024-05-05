from PyQt5 import QtCore, QtGui, QtWidgets
from Componentes.Design import MyDesing
from Componentes.Logic import MyLogic

from datetime import datetime


class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setStyleSheet(
        "background-color: qradialgradient(spread:pad, cx:0.506, cy:0.239727, radius:0.834," 
        "fx:0.506, fy:0.238409, stop:0 rgba(78, 78, 78, 255), stop:1 rgba(55, 55, 55, 255));"
        )
        
        self.central_widget = QtWidgets.QWidget()  
        MainWindow.setCentralWidget(self.central_widget)

        self.my_design = MyDesing()
        self.my_logic = MyLogic(self)

        self.grid_layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # ======================= SpinBoxes (Frame-Layout) =======================
        self.spinbox_frame = QtWidgets.QFrame()
        self.spinbox_frame.setStyleSheet("background-color: black;")
        self.spinbox_frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout = QtWidgets.QHBoxLayout()

        # ======================= SpinBox 1 =======================
        self.spinBox_1 = QtWidgets.QSpinBox()
        self.spinBox_1 = self.my_design.add_spinbox(99)
        self.layout.addWidget(self.spinBox_1)

        # ======================= SpinBox 2 =======================
        self.spinBox_2 = QtWidgets.QSpinBox()
        self.spinBox_2 = self.my_design.add_spinbox(59)
        self.layout.addWidget(self.spinBox_2)

        # ======================= SpinBox 3 =======================
        self.spinBox_3 = QtWidgets.QSpinBox()
        self.spinBox_3 = self.my_design.add_spinbox(59)
        self.layout.addWidget(self.spinBox_3)

        # ===============| 
        self.spinbox_frame.setLayout(self.layout)
        # =========================================================


        # ======================= PuchButtons (Frame-Layout) =======================
        self.button_Frame = QtWidgets.QFrame()
        self.button_Frame.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.button_Frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.button_glayout = QtWidgets.QGridLayout()
        self.button_glayout.setHorizontalSpacing(100)

        # ======================= Button Icons =======================
        icon_start = QtGui.QIcon("./Imagenes/play-button.png")
        icon_pause = QtGui.QIcon("./Imagenes/pause.png")
        icon_clear = QtGui.QIcon("./Imagenes/square-shape.png")

        # ======================= Button Start =======================
        self.button_start = QtWidgets.QPushButton()
        self.button_start = self.my_design.add_button(icon_start)
        self.button_start.setVisible(True)

        def push_button():
            if (self.spinBox_3.value() == 0 and
                self.spinBox_2.value() == 0 and
                self.spinBox_1.value() == 0):
                pass
            else:
                self.my_logic.toggle_visibility()
                self.my_logic.set_spinbox_time()

        self.button_start.clicked.connect(push_button)
        # ======================= Button Pause =======================
        self.button_pause = QtWidgets.QPushButton()
        self.button_pause = self.my_design.add_button(icon_pause)
        self.button_pause.setVisible(False)

        # ======================= Button Clear =======================
        self.button_clear = QtWidgets.QPushButton()
        self.button_clear = self.my_design.add_button(icon_clear)
        self.button_clear.setVisible(False)
        self.button_clear.clicked.connect(self.my_logic.toggle_visibility)

        # ======================= Button GridLayout =======================
        self.button_glayout.addWidget(self.button_start, 1, 2, QtCore.Qt.AlignCenter)
        self.button_glayout.addWidget(self.button_pause, 1, 1, QtCore.Qt.AlignCenter)
        self.button_glayout.addWidget(self.button_clear, 1, 3, QtCore.Qt.AlignCenter)

        self.button_Frame.setLayout(self.button_glayout)

        # ---------------- Asignar Gridlayout ---------------------------
        self.grid_layout.addWidget(self.spinbox_frame, 1, 1, QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.button_Frame, 2, 1, QtCore.Qt.AlignCenter)

        # Obtiene la fecha y hora actual
        ahora = datetime.now()

        # Imprime la fecha y hora actual en el formato deseado
        print("Fecha y hora actual: ", ahora)
        print("Mes: ", ahora.month)
        print("Día: ", ahora.day)
        print("Hora: ", ahora.hour)
        print("Minuto: ", ahora.minute)
        print("Segundo: ", ahora.second)
