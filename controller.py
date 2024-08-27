
from pathlib import Path
from PySide6.QtWidgets import QFileDialog
import markdown

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.setup_connections()

    def setup_connections(self):
        self.view.folder_button.clicked.connect(self.select_folder)
        self.view.prompt_combobox.currentIndexChanged.connect(self.prompt_changed)
        self.view.response_combobox.currentIndexChanged.connect(self.response_changed)
        self.view.system_prompt_combobox.currentIndexChanged.connect(self.system_prompt_changed)
        self.view.system_prompt_button.clicked.connect(self.show_system_prompt)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder:
            self.model.selected_folder = folder
            self.update_folder_label()
            self.update_comboboxes()

    def update_folder_label(self):
        self.view.folder_label.setText(str(self.model.selected_folder))

    def update_comboboxes(self):
        self.view.prompt_combobox.clear()
        self.view.response_combobox.clear()
        self.view.system_prompt_combobox.clear()

        for file in self.model.prompt_files:
            self.view.prompt_combobox.addItem(file.name, file)
            self.view.response_combobox.addItem(file.name, file)
            self.view.system_prompt_combobox.addItem(file.name, file)

    def prompt_changed(self, index):
        selected_prompt = self.view.prompt_combobox.itemData(index)
        self.model.set_selected_prompt(selected_prompt)
        self.view.prompt_text.setPlainText(self.model.selected_prompt_content)

    def response_changed(self, index):
        selected_response = self.view.response_combobox.itemData(index)
        self.model.set_selected_response(selected_response)
        # Convert markdown to HTML
        markdown_content = self.model.selected_response_content
        html_content = markdown.markdown(markdown_content)
        self.view.response_text.setHtml(html_content)

    def system_prompt_changed(self, index):
        selected_system_prompt = self.view.system_prompt_combobox.itemData(index)
        self.model.set_selected_system_prompt(selected_system_prompt)

    def show_system_prompt(self):
        system_prompt_content = self.model.selected_system_prompt_content
        self.view.show_system_prompt_dialog(system_prompt_content)
