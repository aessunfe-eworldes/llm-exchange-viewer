
from pathlib import Path

class Model:
    def __init__(self):
        self._selected_folder = None
        self._selected_prompt = None
        self._selected_response = None
        self._selected_system_prompt = None

    @property
    def selected_folder(self):
        return self._selected_folder

    @selected_folder.setter
    def selected_folder(self, folder_path):
        self._selected_folder = Path(folder_path)
        self._selected_prompt = None
        self._selected_response = None
        self._selected_system_prompt = None

    @property
    def prompt_files(self):
        if self._selected_folder:
            return list(self._selected_folder.glob("*.txt"))
        return []

    @property
    def response_files(self):
        return self.prompt_files

    @property
    def system_prompt_files(self):
        return self.prompt_files

    def load_file_content(self, file_path):
        if file_path:
            with open(file_path, 'r') as file:
                return file.read()
        return ""

    @property
    def selected_prompt_content(self):
        return self.load_file_content(self._selected_prompt)

    @property
    def selected_response_content(self):
        return self.load_file_content(self._selected_response)

    @property
    def selected_system_prompt_content(self):
        return self.load_file_content(self._selected_system_prompt)

    def set_selected_prompt(self, prompt_path):
        self._selected_prompt = prompt_path

    def set_selected_response(self, response_path):
        self._selected_response = response_path

    def set_selected_system_prompt(self, system_prompt_path):
        self._selected_system_prompt = system_prompt_path
