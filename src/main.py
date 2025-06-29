
import sys
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QTableWidgetItem
from src.organizer import FileOrganizer
from src.settings import SettingsManager
from src.ui import MainUI, SettingsDialog
from src.scheduler import FileOrganizerScheduler

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileOrganizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.setGeometry(100, 100, 800, 600)

        self.organizer = FileOrganizer()
        self.settings_manager = SettingsManager()
        self.main_ui = MainUI()
        self.status_log = self.main_ui.status_log
        self.scheduler = FileOrganizerScheduler(
            self.organizer,
            lambda: self.main_ui.folder_path_input.text(),
            lambda: self.settings_manager.get_setting("auto_organize_interval"),
            self.log_status
        )

        self.setup_ui()
        self.create_menu()
        self.connect_signals()
        self.scheduler.start_scheduler() # Start scheduler on app launch

    def closeEvent(self, event):
        self.scheduler.stop_scheduler() # Stop scheduler on app close
        event.accept()

    def setup_ui(self):
        self.setCentralWidget(self.main_ui)

    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        settings_menu = menubar.addMenu("Settings")
        open_settings_action = QAction("Open Settings", self)
        open_settings_action.triggered.connect(self.open_settings)
        settings_menu.addAction(open_settings_action)

    def connect_signals(self):
        self.main_ui.browse_button.clicked.connect(self.browse_folder)
        self.main_ui.organize_button.clicked.connect(self.organize_files)
        self.main_ui.undo_button.clicked.connect(self.undo_organization)

    def browse_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_selected:
            self.main_ui.folder_path_input.setText(folder_selected)

    def open_settings(self):
        settings_dialog = SettingsDialog(self.settings_manager, self)
        if settings_dialog.exec_():
            self.scheduler.stop_scheduler() # Stop and restart scheduler if settings changed
            self.scheduler.start_scheduler()

    def undo_organization(self):
        self.log_status("Attempting to undo last organization...")
        message, log_entries = self.organizer.undo_last_organization()
        self.log_status(message)
        for entry in log_entries:
            self.log_status(entry)
        self.main_ui.organized_files_table.setRowCount(0) # Clear table on undo

    def organize_files(self):
        source_folder = self.main_ui.folder_path_input.text()
        if not source_folder:
            self.log_status("Please select a folder first.")
            return
        self.log_status(f"Organizing files in: {source_folder}")
        
        status_message, moved_files = self.organizer.organize_folder(source_folder)
        self.log_status(status_message)
        
        self.main_ui.organized_files_table.setRowCount(0) # Clear previous results
        for row, file_info in enumerate(moved_files):
            self.main_ui.organized_files_table.insertRow(row)
            self.main_ui.organized_files_table.setItem(row, 0, QTableWidgetItem(file_info['file_name']))
            self.main_ui.organized_files_table.setItem(row, 1, QTableWidgetItem(file_info['time_created']))

    def log_status(self, message):
        logging.info(message)
        self.status_log.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())
