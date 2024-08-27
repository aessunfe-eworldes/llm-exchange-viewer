
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QFileDialog, QDialog, QDialogButtonBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextDocument

class View(QWidget):
    def __init__(self):
        super().__init__()

        # Layout setup
        self.setWindowTitle("LLM Exchange Viewer")
        self.layout = QVBoxLayout(self)

        # Top bar
        self.top_bar = QHBoxLayout()

        self.folder_label = QLabel("No folder selected")
        self.top_bar.addWidget(self.folder_label)

        self.folder_button = QPushButton("Folder")
        self.top_bar.addWidget(self.folder_button)

        self.prompt_label = QLabel("Prompt:")
        self.top_bar.addWidget(self.prompt_label)

        self.prompt_combobox = QComboBox()
        self.top_bar.addWidget(self.prompt_combobox)

        self.response_label = QLabel("Response:")
        self.top_bar.addWidget(self.response_label)

        self.response_combobox = QComboBox()
        self.top_bar.addWidget(self.response_combobox)

        self.system_prompt_label = QLabel("System:")
        self.top_bar.addWidget(self.system_prompt_label)

        self.system_prompt_combobox = QComboBox()
        self.top_bar.addWidget(self.system_prompt_combobox)

        self.layout.addLayout(self.top_bar)

        # Scrollable areas
        self.prompt_text = QTextEdit()
        self.prompt_text.setReadOnly(True)
        self.layout.addWidget(self.prompt_text)

        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        self.layout.addWidget(self.response_text)

        # Show System Prompt Button
        self.system_prompt_button = QPushButton("Show System Prompt")
        self.layout.addWidget(self.system_prompt_button, alignment=Qt.AlignRight)

    def show_system_prompt_dialog(self, system_prompt_content):
        dialog = QDialog(self)
        dialog.setWindowTitle("System Prompt")
        dialog_layout = QVBoxLayout(dialog)

        system_prompt_text = QTextEdit()
        system_prompt_text.setReadOnly(True)
        system_prompt_text.setText(system_prompt_content)
        dialog_layout.addWidget(system_prompt_text)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(dialog.accept)
        dialog_layout.addWidget(buttons)

        dialog.exec_()
