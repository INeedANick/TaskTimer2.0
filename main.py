import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5 import QtCore
from Apps.Timer import TimerApp
from Apps.Tasking import TaskingApp
from TimerComponents.Logic import MyLogic
from TaskingComponents.Logic import MyLogic as Task_logic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QMainWindow {background-color: qradialgradient(spread:pad," 
                           "cx:0.506, cy:0.239727, radius:0.834,fx:0.506, fy:0.238409," 
                           "stop:0 rgba(78, 78, 78, 255), stop:1 rgba(55, 55, 55, 255));}")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # ======================= Starting Apps =======================
        self.timer_app = None
        self.tasking_app = None

        self.i = None  
        self.j = None 

        self.setWindowTitle("Cronómetro y Gestor de Tareas")
        self.resize(800, 600)

    def showEvent(self, event):
        super().showEvent(event)
        self.initialize_apps()

    def initialize_apps(self):
        # ======================= Timer App =======================
        if MyLogic.is_final_time_null():
            self.i = 0  
        else:
            self.i = 1  
        
        if not self.timer_app:
            self.timer_app = TimerApp(self)
            self.layout.addWidget(self.timer_app, 0, 0, QtCore.Qt.AlignHCenter)

        # ======================= Tasking App =======================
        if Task_logic.is_tasking_null():
            self.j = 0 
        else:
            self.j = 1 
        
        if not self.tasking_app:
            self.tasking_app = TaskingApp(self)
            self.layout.addWidget(self.tasking_app, 1, 0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.layout.setColumnStretch(0, 1)
        self.layout.setRowStretch(1, 1)

def main():
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
