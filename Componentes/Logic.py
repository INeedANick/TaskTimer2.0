from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QRect, QSize

class MyLogic(QtWidgets.QFrame):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  
        
    def toggle_visibility(self):
        sender = self.sender()
        
        if sender == self.main_window.button_start:
            self.main_window.button_start.setVisible(False)
            self.main_window.button_clear.setVisible(True)
            self.main_window.button_pause.setVisible(True)
        elif sender == self.main_window.button_clear:
            self.main_window.button_clear.setVisible(False)
            self.main_window.button_pause.setVisible(False)
            self.main_window.button_start.setVisible(True)