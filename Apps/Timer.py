from PyQt5 import QtWidgets, QtGui, QtCore
from TimerComponents.Desing import MyDesing
from TimerComponents.Logic import MyLogic

class TimerApp(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.my_design = MyDesing()
        self.my_logic = MyLogic(self)
        self.setMinimumSize(300, 200)  # Tamaño mínimo
        self.setMaximumSize(500, 200)
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

        self.spinbox_frame.setLayout(self.layout)
        
        self.gl_buttons_crono = QtWidgets.QGridLayout()
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
                self.my_logic.set_time_end()

        self.button_start.clicked.connect(push_button)

        # ======================= Button Pause =======================
        self.button_pause = QtWidgets.QPushButton()
        self.button_pause = self.my_design.add_button(icon_pause)
        self.button_pause.setVisible(False)
        self.button_pause.clicked.connect(self.my_logic.toggle_visibility)
        self.button_pause.clicked.connect(self.my_logic.pause_spinboxes)

        # ======================= Button Clear =======================
        self.button_clear = QtWidgets.QPushButton()
        self.button_clear = self.my_design.add_button(icon_clear)
        self.button_clear.setVisible(False)
        self.button_clear.clicked.connect(self.my_logic.toggle_visibility)
        self.button_clear.clicked.connect(self.my_logic.clean_spinboxes)

        # ======================= Button GridLayout =======================
        self.gl_buttons_crono.addWidget(self.button_start, 1, 2, QtCore.Qt.AlignCenter)
        self.gl_buttons_crono.addWidget(self.button_pause, 1, 1, QtCore.Qt.AlignCenter)
        self.gl_buttons_crono.addWidget(self.button_clear, 1, 3, QtCore.Qt.AlignCenter)

        # ======================= Main Layout =======================
        self.main_gridlayout = QtWidgets.QGridLayout(self)
        self.main_gridlayout.addWidget(self.spinbox_frame, 0, 0)
        self.main_gridlayout.addLayout(self.gl_buttons_crono, 1, 0)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.main_gridlayout)

        # ======================= Restore Timer =======================
        if MainWindow.i == 1:
            self.my_logic.set_time()
            self.my_logic.set_spinbox_time()
            self.button_start.click()
