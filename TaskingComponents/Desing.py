from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets, QtGui, QtCore

class MyDesing():
    def TextEdit(self):
        style = ("QTextEdit { border: none; border-bottom: 1px solid black; }; background: transparent;")
        font = QtGui.QFont("Sans", 12)
        #font.setBold(True)  
        text_color = QtGui.QColor(255, 255, 255)

        text_edit = QtWidgets.QTextEdit()
        text_edit.setFont(font)
        text_edit.setStyleSheet(style)
        text_edit.setTextColor(text_color)

        return text_edit

    def set_text_color(self, text_edit):
        # Establecer el color de texto en blanco
        text_color = QtGui.QColor(255, 255, 255)
        text_edit.setTextColor(text_color)
    

