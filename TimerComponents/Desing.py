from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets, QtGui, QtCore

class MyDesing():
    # ===================== Add Spinbox =====================
    def add_spinbox(self, maximun):
            style = ("""
                QSpinBox {
                    color: #bfbfbf;
                    border: none;
                    selection-background-color: transparent;
                }
                QSpinBox::focus {
                    outline: none;
                }
                """)
            font = QtGui.QFont("Bahnschrift", 80)
            spinBox = QtWidgets.QSpinBox()
            spinBox.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            spinBox.setFont(QtGui.QFont("", 72))
            spinBox.setEnabled(True)
            spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            spinBox.setStyleSheet(style)
            spinBox.setMaximum(maximun)
            spinBox.setFont(font)

            palette = spinBox.palette()
            color_transparente = QtGui.QColor(0, 0, 0, 0)    
            palette.setColor(QtGui.QPalette.Highlight, color_transparente)
            spinBox.setPalette(palette)

            return spinBox
    
    # ===================== Add Buttons =====================
    def add_button(self, icon):
        style = ("QPushButton {background-color: qradialgradient(spread:pad, cx:0.506," 
                                "cy:0.239727, radius:0.834, fx:0.506, fy:0.238409, stop:0 rgba(40, 40, 40, 255),"
                                "stop:1 rgba(18, 18, 18, 255)); border: 1.8px solid black; "
                                "border-radius: 29.4px}"
                                "QPushButton:hover {background-color: white}" 
                                "QPushButton:pressed {background-color: grey;}")
        
        button = QtWidgets.QPushButton()
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(24, 24))

        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setFixedWidth(58)
        button.setFixedHeight(58)
        button.setMask(QtGui.QRegion(QtCore.QRect(-1, -1, 59, 59), QtGui.QRegion.Ellipse))
        button.setStyleSheet(style) 

        return button
