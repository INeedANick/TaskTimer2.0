import sys
import json
import uuid  # Para generar identificadores únicos
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit, QComboBox,
    QWidget, QVBoxLayout, QScrollArea, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)

        self.json_file = "tasks.json"

        # Leer JSON al iniciar la aplicación
        self.tasks = self.load_json()

        # Layout principal
        self.main_layout = QVBoxLayout()

        # Botón para agregar nuevo QTextEdit y QComboBox
        self.add_button = QPushButton("Agregar QTextEdit y QComboBox")
        self.add_button.clicked.connect(self.add_text_edit_combo)

        self.main_layout.addWidget(self.add_button)

        # Área de desplazamiento
        self.scroll_area = QScrollArea()
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll_area)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

        # Cargar tareas desde JSON
        self.load_tasks()

    def load_json(self):
        """Carga las tareas desde el archivo JSON."""
        try:
            with open(self.json_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_json(self):
        """Guarda las tareas actuales en el archivo JSON."""
        with open(self.json_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_text_edit_combo(self):
        # Generar un identificador único para la tarea
        task_id = str(uuid.uuid4())

        # Crear un widget que contiene QTextEdit y QComboBox
        widget = QWidget()
        layout = QVBoxLayout()

        text_edit = QTextEdit()
        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Eliminar"])

        combo_box.currentTextChanged.connect(lambda text, w=widget, id=task_id: self.combo_box_changed(text, w, id))

        layout.addWidget(text_edit)
        layout.addWidget(combo_box)
        widget.setLayout(layout)

        self.scroll_area_layout.addWidget(widget)

        # Agregar la nueva tarea al diccionario de tareas
        self.tasks[task_id] = {
            "content": text_edit.toPlainText()
        }
        self.save_json()

    def combo_box_changed(self, text, widget, task_id):
        if text == "Eliminar":
            reply = QMessageBox.question(self, 'Eliminar', '¿Estás seguro de que deseas eliminar este elemento?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Eliminar el widget
                self.scroll_area_layout.removeWidget(widget)
                widget.deleteLater()

                # Eliminar la tarea del diccionario
                if task_id in self.tasks:
                    del self.tasks[task_id]
                    self.save_json()

    def load_tasks(self):
        """Carga las tareas desde el JSON al iniciar la aplicación."""
        for task_id, task_data in self.tasks.items():
            widget = QWidget()
            layout = QVBoxLayout()

            text_edit = QTextEdit()
            text_edit.setText(task_data.get("content", ""))
            combo_box = QComboBox()
            combo_box.addItems(["Option 1", "Option 2", "Eliminar"])

            combo_box.currentTextChanged.connect(lambda text, w=widget, id=task_id: self.combo_box_changed(text, w, id))

            layout.addWidget(text_edit)
            layout.addWidget(combo_box)
            widget.setLayout(layout)

            self.scroll_area_layout.addWidget(widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
