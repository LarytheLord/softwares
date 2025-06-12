import os
import shutil
from file_manager import FileManager

class FileOrganizer:
    def __init__(self):
        self.file_manager = FileManager()
        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Executables": [".exe", ".dmg", ".app", ".deb", ".rpm"],
            "Other": [] # Catch-all for uncategorized files
        }

    def organize_folder(self, source_folder):
        if not os.path.isdir(source_folder):
            return "Error: Source folder does not exist.", []

        moved_files = []
        files_to_organize = self.file_manager.get_files_in_folder(source_folder)

        for item_path in files_to_organize:
            item_name = os.path.basename(item_path)
            file_extension = self.file_manager.get_file_extension(item_name)
            destination_folder_name = self._get_destination_folder(file_extension)
            
            destination_path = os.path.join(source_folder, destination_folder_name)
            success, msg = self.file_manager.create_directory(destination_path)
            if not success:
                moved_files.append(msg)
                continue
            
            success, msg = self.file_manager.move_file(item_path, os.path.join(destination_path, item_name))
            moved_files.append(msg)
        return "Organization complete.", moved_files

    def _get_destination_folder(self, extension):
        for category, extensions in self.categories.items():
            if extension in extensions:
                return category
        return "Other"