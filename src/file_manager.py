import os
import shutil

class FileManager:
    def __init__(self):
        pass

    def move_file(self, source_path, destination_path):
        try:
            shutil.move(source_path, destination_path)
            return True, f"Moved: {os.path.basename(source_path)} to {os.path.basename(os.path.dirname(destination_path))}"
        except Exception as e:
            return False, f"Error moving {os.path.basename(source_path)}: {e}"

    def create_directory(self, path):
        try:
            os.makedirs(path, exist_ok=True)
            return True, f"Created directory: {path}"
        except Exception as e:
            return False, f"Error creating directory {path}: {e}"

    def get_file_extension(self, filename):
        return os.path.splitext(filename)[1].lower()

    def get_files_in_folder(self, folder_path):
        files = []
        if os.path.isdir(folder_path):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    files.append(item_path)
        return files