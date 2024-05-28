from PyQt5 import QtCore, QtGui, QtWidgets
from Componentes.Design import MyDesing
from Componentes.Logic import MyLogic

class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 620)
        MainWindow.setStyleSheet(
        "background-color: qradialgradient(spread:pad, cx:0.506, cy:0.239727, radius:0.834," 
        "fx:0.506, fy:0.238409, stop:0 rgba(78, 78, 78, 255), stop:1 rgba(55, 55, 55, 255));"
        )

        # ========================================================================
        self.central_widget = QtWidgets.QWidget()  
        MainWindow.setCentralWidget(self.central_widget)

        self.gl_global = QtWidgets.QGridLayout()
        self.gl_global.setContentsMargins(0, 25, 0, 0)
        self.central_widget.setLayout(self.gl_global)

        self.gl_upper_main = QtWidgets.QGridLayout()
        self.gl_upper_main.setContentsMargins(10, 2, 10, 2)
        self.gl_global.addLayout(self.gl_upper_main, 1, 1)

        self.gl_crono = QtWidgets.QGridLayout()
        self.gl_upper_main.addLayout(self.gl_crono, 1, 3, QtCore.Qt.AlignCenter)

        self.gl_buttons_crono = QtWidgets.QGridLayout()
        self.gl_buttons_crono.setHorizontalSpacing(80)
        self.gl_buttons_crono.setContentsMargins(0, 0, 0, 10)
        self.gl_crono.addLayout(self.gl_buttons_crono, 2, 2, QtCore.Qt.AlignCenter)

        # ========================================================================
        self.my_design = MyDesing()
        self.my_logic = MyLogic(self)
        # ========================================================================

        # ======================= SpinBoxes (Frame-Layout) =======================
        self.spinbox_frame = QtWidgets.QFrame()
        self.spinbox_frame.setStyleSheet("background-color: black;")
        self.spinbox_frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gl_crono.addWidget(self.spinbox_frame, 1, 2, QtCore.Qt.AlignCenter)

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
        # =========================================================

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

        # ======================= Scroll Area =======================
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:0, y2:0.5,
                stop:0 rgba(22, 22, 22, 255), stop:0 rgba(18, 18, 18, 255));
            }
            QScrollArea {
                border: none;
            }
        """)
        self.scroll_area.setWidgetResizable(True)
        self.gl_global.addWidget(self.scroll_area, 2, 1)

        # ======================= Buttons Tasking Area =======================
        self.add_task = QtWidgets.QPushButton("+ Task")
        self.add_task.clicked.connect(self.my_logic.add_task)
        self.add_group = QtWidgets.QPushButton("+ Gruop")

        self.up_task = QtWidgets.QPushButton("<")
        self.down_task = QtWidgets.QPushButton(">")

        self.gl_upper_main.addWidget(self.add_task, 1, 1, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        self.gl_upper_main.addWidget(self.add_group, 1, 2, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        self.gl_upper_main.addWidget(self.up_task, 1, 4, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.gl_upper_main.addWidget(self.down_task, 1, 5, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        # ======================= Restore Timer =======================
        if MainWindow.i == 1:
            self.my_logic.set_time()
            self.my_logic.set_spinbox_time()
            self.button_start.click()

    