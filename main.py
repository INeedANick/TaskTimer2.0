import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from Qt import Ui_MainWindow 

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.timer = None

        self.installEventFilter(self)
    
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() == QtCore.Qt.WindowState.WindowNoState:
                print("La ventana principal se ha restaurado.")
                self.my_logic.rest_time()
            elif self.windowState() == QtCore.Qt.WindowState.WindowMinimized:
                print("La ventana principal se ha minimizado.")

        return super().eventFilter(source, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())