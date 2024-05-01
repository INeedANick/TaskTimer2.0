from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from Componentes.SpinBox import MySpinBox
import sys

class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setStyleSheet(
        "background-color: qradialgradient(spread:pad, cx:0.506, cy:0.239727, radius:0.834," 
        "fx:0.506, fy:0.238409, stop:0 rgba(78, 78, 78, 255), stop:1 rgba(55, 55, 55, 255));"
        )
        
        self.central_widget = QtWidgets.QWidget()  
        MainWindow.setCentralWidget(self.central_widget)

        self.grid_layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.my_spinbox = MySpinBox()
        self.my_spinbox.setStyleSheet("background-color: black;")
        self.my_spinbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.grid_layout.addWidget(self.my_spinbox, 1, 1, QtCore.Qt.AlignCenter)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec_())