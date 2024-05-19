import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from Qt import Ui_MainWindow 
from Componentes.Logic import MyLogic

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.timer = None

    def showEvent(self, event):
        super().showEvent(event)
        if MyLogic.is_final_time_null():
            print("final_time es null")
        else:
            print("final_time tiene un valor")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())