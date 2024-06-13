from PyQt5 import QtWidgets, QtCore
import json
from TaskingComponents.Desing import MyDesing

class MyLogic(QtWidgets.QFrame):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.my_design = MyDesing()
    
    def add_text_edit(self, text='', checked=False):
        if not isinstance(text, str):
            text = ''
        # Contenedor para QTextEdit y QCheckBox
        frame = QtWidgets.QFrame(self)
        frameLayout = QtWidgets.QHBoxLayout(frame)
        frameLayout.setContentsMargins(0, 0, 0, 0)
        frame.setFixedHeight(30)

        # Crear un QCheckBox
        checkBox = QtWidgets.QCheckBox(self)
        checkBox.setChecked(checked)
        frameLayout.addWidget(checkBox)

        # Crear un QTextEdit
        textEdit = QtWidgets.QTextEdit(self)
        textEdit.setFixedHeight(40)
        textEdit = self.my_design.TextEdit()
        textEdit.textChanged.connect(lambda: self.my_design.set_text_color(textEdit))
        textEdit.installEventFilter(self)  # Instalar un filtro de eventos para capturar focusOutEvent
        frameLayout.addWidget(textEdit)
        textEdit.setPlainText(text)

        self.main_window.text_edit_layout.insertWidget(self.main_window.text_edit_layout.count() - 1, frame)
        textEdit.setFocus()
    
    def saveData(self):
        data = []
        for i in range(self.main_window.text_edit_layout.count()):
            frame = self.main_window.text_edit_layout.itemAt(i).widget()
            if frame:
                textEdit = frame.findChild(QtWidgets.QTextEdit)
                checkBox = frame.findChild(QtWidgets.QCheckBox)
                data.append({
                    'text': textEdit.toPlainText(),
                    'checked': checkBox.isChecked()
                })
        
        with open("TaskingComponents/BD.json", 'w') as f:
            json.dump(data, f, indent=4)

    def loadData(self):
        try:
            with open("TaskingComponents/BD.json", 'r') as f:
                data = json.load(f)
            
            for item in data:
                self.add_text_edit(text=item['text'], checked=item['checked'])
        except FileNotFoundError:
            pass

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusOut:
            self.saveData()  # Llamar a saveData cuando el QTextEdit pierda el foco
        return super().eventFilter(obj, event)


    def is_tasking_null():
        ruta_json = 'TaskingComponents/BD.json'
        try:
            with open(ruta_json, 'r') as file:
                data = json.load(file)
                
                # Si los datos son una lista, busca si algún elemento contiene 'Task'
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict) and 'Task' in item:
                            final_time_data = item['Task']
                            return final_time_data is None
                    # Si ningún elemento contiene 'Task', retorna False
                    return False
                
                # Si los datos son un diccionario, busca 'Task' directamente
                elif isinstance(data, dict):
                    final_time_data = data.get('Task', None)
                    return final_time_data is None
                
                # Si los datos no son ni lista ni diccionario, retorna False
                else:
                    return False
        except FileNotFoundError:
            # Retorna True si el archivo no se encuentra
            return True
        except json.JSONDecodeError:
            # Retorna True si hay un error al cargar el JSON (formato incorrecto)
            return True
        except Exception as e:
            # Maneja cualquier otra excepción inesperada
            print(f"Ocurrió un error inesperado: {e}")
            return True
