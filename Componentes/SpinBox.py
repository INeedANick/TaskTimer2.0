from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets, QtGui, QtCore

class MySpinBox(QFrame):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QHBoxLayout()
        font = QtGui.QFont("Bahnschrift", 80)

        def add_spinbox(maximun):
            spinBox = QtWidgets.QSpinBox()
            spinBox.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            spinBox.setFont(QtGui.QFont("", 72))
            spinBox.setEnabled(True)
            spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            spinBox.setStyleSheet("color: #FFFFFF")
            spinBox.setMaximum(maximun)
            spinBox.setFont(font)

            palette = spinBox.palette()
            color_transparente = QtGui.QColor(0, 0, 0, 0)    
            palette.setColor(QtGui.QPalette.Highlight, color_transparente)
            spinBox.setPalette(palette)

            return spinBox

        # ------------------ SpinBox 1 -------------------------------
        self.spinBox_1 = QtWidgets.QSpinBox()
        self.spinBox_1 = add_spinbox(99)

        # ------------------ SpinBox 2 -------------------------------
        self.spinBox_2 = QtWidgets.QSpinBox()
        self.spinBox_2 = add_spinbox(59)

        # ------------------ SpinBox 3 -------------------------------
        self.spinBox_3 = QtWidgets.QSpinBox()
        self.spinBox_3 = add_spinbox(59)

        # ---------------- Asignar a layout ---------------------------
        self.layout.addWidget(self.spinBox_1)
        self.layout.addWidget(self.spinBox_2)
        self.layout.addWidget(self.spinBox_3)
        
        self.setLayout(self.layout)

    def set_spinbox_time(self):
        def decrement_spinbox():
            current_value_seconds = self.spinBox_3.value()
            current_value_minutes = self.spinBox_2.value()
            current_value_hours = self.spinBox_1.value()
            if current_value_seconds > 0:
                self.spinBox_3.setValue(current_value_seconds - 1)
            else:
                self.spinBox_3.setValue(0)
                if current_value_minutes > 0:
                    self.spinBox_2.setValue(current_value_minutes - 1)
                    self.spinBox_3.setValue(59)
                elif (current_value_seconds == 0) and (current_value_minutes == 0) and (current_value_hours > 0):
                    self.spinBox_1.setValue(current_value_hours - 1)
                    self.spinBox_2.setValue(59)
                    self.spinBox_3.setValue(59)
                else:
                    self.timer.stop()  # Detener el temporizador cuando se complete el tiempo

        if self.timer is None:
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(decrement_spinbox)