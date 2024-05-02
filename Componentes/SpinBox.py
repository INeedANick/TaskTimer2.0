from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets, QtGui, QtCore

class MySpinBox(QFrame):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QHBoxLayout()
        font = QtGui.QFont("Bahnschrift", 80)  

        # ------------------ SpinBox 1 -------------------------------
        self.spinBox_1 = QtWidgets.QSpinBox()
        self.spinBox_1.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.spinBox_1.setFont(QtGui.QFont("", 72))
        self.spinBox_1.setEnabled(True)
        self.spinBox_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_1.setStyleSheet("color: #FFFFFF")
        self.spinBox_1.setMaximum(99)
        self.spinBox_1.setFont(font)

        # ------------------ SpinBox 2 -------------------------------
        self.spinBox_2 = QtWidgets.QSpinBox()
        self.spinBox_2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.spinBox_2.setFont(QtGui.QFont("", 72))
        self.spinBox_2.setEnabled(True)
        self.spinBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_2.setStyleSheet("color: #FFFFFF")
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setFont(font)


        # ------------------ SpinBox 3 -------------------------------
        self.spinBox_3 = QtWidgets.QSpinBox()
        self.spinBox_3.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.spinBox_3.setFont(QtGui.QFont("", 72))
        self.spinBox_3.setEnabled(True)
        self.spinBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_3.setStyleSheet("color: #FFFFFF")
        self.spinBox_3.setMaximum(59)
        self.spinBox_3.setFont(font)

        # Cambia el color de resaltado (highlight) a tu preferencia (por ejemplo, rojo)
        palette = self.spinBox_1.palette()
        color_transparente = QtGui.QColor(0, 0, 0, 0)    
        palette.setColor(QtGui.QPalette.Highlight, color_transparente)
        self.spinBox_1.setPalette(palette)
        self.spinBox_2.setPalette(palette)
        self.spinBox_3.setPalette(palette)

        # ---------------- Asignar a layout ---------------------------
        self.layout.addWidget(self.spinBox_1)
        self.layout.addWidget(self.spinBox_2)
        self.layout.addWidget(self.spinBox_3)
        
        self.setLayout(self.layout)