from PyQt5 import QtWidgets, QtGui, QtCore

class MyLogic(QtWidgets.QFrame):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.timer = None  

    # ===================== Buttons Visibility =====================
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
        elif sender == self.main_window.button_pause:
            self.main_window.button_clear.setVisible(False)
            self.main_window.button_pause.setVisible(False)
            self.main_window.button_start.setVisible(True)

    # ====================== SpinBox Time ======================
    def set_spinbox_time(self):
        def decrement_spinbox(self):
            self.current_seconds = self.main_window.spinBox_3.value()
            self.current_minutes = self.main_window.spinBox_2.value()
            self.current_hours = self.main_window.spinBox_1.value()

            if self.current_seconds > 0:
                self.main_window.spinBox_3.setValue(self.current_seconds - 1)
            elif self.current_minutes > 0:
                self.main_window.spinBox_2.setValue(self.current_minutes - 1)
                self.main_window.spinBox_3.setValue(59)
            elif self.current_hours > 0:
                self.main_window.spinBox_1.setValue(self.current_hours - 1)
                self.main_window.spinBox_2.setValue(59)
                self.main_window.spinBox_3.setValue(59)
            else:
                self.timer.stop()
        
        if self.timer is None:
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(lambda: decrement_spinbox(self))
        self.timer.start(1000)

    # ====================== Clean SpinBoxes ======================
    def clean_spinboxes(self):
        self.main_window.spinBox_3.setValue(0)
        self.main_window.spinBox_2.setValue(0)
        self.main_window.spinBox_1.setValue(0)

    def pause_spinboxes(self):
        self.timer.stop()