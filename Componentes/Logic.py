from PyQt5 import QtWidgets, QtCore
from datetime import datetime, timedelta
import pandas as pd
import json

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
            self.main_window.spinBox_1.setEnabled(False)
            self.main_window.spinBox_2.setEnabled(False)
            self.main_window.spinBox_3.setEnabled(False)
        elif sender == self.main_window.button_clear:
            self.main_window.button_clear.setVisible(False)
            self.main_window.button_pause.setVisible(False)
            self.main_window.button_start.setVisible(True)
            self.main_window.spinBox_1.setEnabled(True)
            self.main_window.spinBox_2.setEnabled(True)
            self.main_window.spinBox_3.setEnabled(True)
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
                self.main_window.button_clear.setVisible(False)
                self.main_window.button_pause.setVisible(False)
                self.main_window.button_start.setVisible(True)
                self.main_window.spinBox_1.setEnabled(True)
                self.main_window.spinBox_2.setEnabled(True)
                self.main_window.spinBox_3.setEnabled(True)
        
        if self.timer is None:
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(lambda: decrement_spinbox(self))
        self.timer.start(1000)

    # ====================== Clean SpinBoxes ======================
    def clean_spinboxes(self):
        self.main_window.spinBox_3.setValue(0)
        self.main_window.spinBox_2.setValue(0)
        self.main_window.spinBox_1.setValue(0)

        ruta_json = 'Componentes/BD.json'
        data = {
                "final_time": None
            }

        with open(ruta_json, 'w') as file:
            json.dump(data, file, indent=4)

    # ====================== Pause SpinBoxes ======================
    def pause_spinboxes(self):
        self.timer.stop()

    # ====================== Save Time ======================
    def set_time_end(self):
        ruta_json = 'Componentes/BD.json'

        now = datetime.now()
        current_seconds = self.main_window.spinBox_3.value()
        current_minutes = self.main_window.spinBox_2.value()
        current_hours = self.main_window.spinBox_1.value()

        add_time = timedelta(hours=current_hours, 
                             minutes=current_minutes, 
                             seconds=current_seconds)
        final_time = now + add_time

        data = {
            "final_time": {
                "MES": final_time.month,
                "DIA": final_time.day,
                "HORA": final_time.hour,
                "MINs": final_time.minute,
                "SEGs": final_time.second
            }
        }

        with open(ruta_json, 'w') as file:
            json.dump(data, file, indent=4)
    
    # ====================== Verificar Final Time ======================
    def is_final_time_null():
        ruta_json = 'Componentes/BD.json'
        try:
            with open(ruta_json, 'r') as file:
                data = json.load(file)
                final_time_data = data.get('final_time')
                return final_time_data is None
        except (FileNotFoundError, KeyError, ValueError):
            return True

    if is_final_time_null():
        print("final_time es null")
    else:
        print("final_time tiene un valor")

    def add_task(self):
        new_te = QtWidgets.QTextEdit()
        self.main_window.scroll_area.setWidget(new_te)