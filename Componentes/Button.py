from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QRect, QSize

class MyButton(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        self.Glayout = QtWidgets.QGridLayout()
        self.Glayout.setHorizontalSpacing(80)

        icon_start = QtGui.QIcon("./Imagenes/play-button.png")
        icon_pause = QtGui.QIcon("./Imagenes/pause.png")
        icon_clear = QtGui.QIcon("./Imagenes/square-shape.png")

        def add_button(icon):
            style = ("QPushButton {background-color: qradialgradient(spread:pad, cx:0.506," 
                                    "cy:0.239727, radius:0.834, fx:0.506, fy:0.238409, stop:0 rgba(40, 40, 40, 255),"
                                    "stop:1 rgba(18, 18, 18, 255)); border: 1.8px solid black; "
                                    "border-radius: 29.4px}"
                                    "QPushButton:hover {background-color: white}" 
                                    "QPushButton:pressed {background-color: grey;}")
            
            button = QtWidgets.QPushButton()
            button.setIcon(icon)
            button.setIconSize(QSize(24, 24))

            button.setCursor(Qt.PointingHandCursor)
            button.setFixedWidth(58)
            button.setFixedHeight(58)
            button.setMask(QtGui.QRegion(QRect(-1, -1, 59, 59), QtGui.QRegion.Ellipse))
            button.setStyleSheet(style) 

            return button

        # ------------------ Button Start -------------------------------
        self.button_start = QtWidgets.QPushButton()
        self.button_start = add_button(icon_start)
        self.button_start.setVisible(True)
        self.button_start.clicked.connect(self.toggle_visibility)

        # ------------------ Button Pause -------------------------------
        self.button_pause = QtWidgets.QPushButton()
        self.button_pause = add_button(icon_pause)
        self.button_pause.setVisible(False)

        # ------------------ Button Clear -------------------------------
        self.button_clear = QtWidgets.QPushButton()
        self.button_clear = add_button(icon_clear)
        self.button_clear.setVisible(False)
        self.button_clear.clicked.connect(self.toggle_visibility)

        # ---------------- Asignar a layout ---------------------------
        self.Glayout.addWidget(self.button_start, 1, 2, QtCore.Qt.AlignCenter)
        self.Glayout.addWidget(self.button_pause, 1, 1, QtCore.Qt.AlignCenter)
        self.Glayout.addWidget(self.button_clear, 1, 3, QtCore.Qt.AlignCenter)

        self.setLayout(self.Glayout)

    def toggle_visibility(self):
        if self.sender() == self.button_start:
            self.button_start.setVisible(False)
            self.button_clear.setVisible(True)
            self.button_pause.setVisible(True)
        elif self.sender() == self.button_clear:
            self.button_clear.setVisible(False)
            self.button_pause.setVisible(False)
            self.button_start.setVisible(True)