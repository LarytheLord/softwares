from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Folder selection
        folder_layout = QHBoxLayout()
        self.folder_label = QLabel("Folder:")
        self.folder_path_input = QLineEdit()
        self.browse_button = QPushButton("Browse...")
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.folder_path_input)
        folder_layout.addWidget(self.browse_button)
        self.layout.addLayout(folder_layout)

        # Organize button
        self.organize_button = QPushButton("Organize")
        self.layout.addWidget(self.organize_button)

        # Status log
        self.status_log = QTextEdit()
        self.status_log.setReadOnly(True)
        self.layout.addWidget(self.status_log)