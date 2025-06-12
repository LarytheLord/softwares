import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import MainUI
from organizer import FileOrganizer

class FileOrganizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.setGeometry(100, 100, 800, 600)

        self.main_ui = MainUI()
        self.setCentralWidget(self.main_ui)

        self.file_organizer = FileOrganizer()
        self.connect_signals()

    def connect_signals(self):
        self.main_ui.browse_button.clicked.connect(self.browse_folder)
        self.main_ui.organize_button.clicked.connect(self.organize_files)

    def browse_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_selected:
            self.main_ui.folder_path_input.setText(folder_selected)

    def organize_files(self):
        folder_path = self.main_ui.folder_path_input.text()
        if not folder_path:
            self.main_ui.status_log.append("Please select a folder first.")
            return
        self.main_ui.status_log.append(f"Organizing files in: {folder_path}")
        
        status_message, moved_files = self.file_organizer.organize_folder(folder_path)
        self.main_ui.status_log.append(status_message)
        for file_info in moved_files:
            self.main_ui.status_log.append(file_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())