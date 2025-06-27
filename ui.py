from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit,
                             QTextEdit, QFileDialog, QTabWidget, QFormLayout, QRadioButton, QButtonGroup, QLabel, QDialog, QDialogButtonBox, QMessageBox, QListWidget, QTableWidget)

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
        self.organize_button = QPushButton("Organize Files")
        self.organize_button.setFixedHeight(40)
        self.organize_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; border-radius: 8px;")
        self.layout.addWidget(self.organize_button)

        self.undo_button = QPushButton("Undo Last Organization")
        self.undo_button.setFixedHeight(40)
        self.undo_button.setStyleSheet("background-color: #f44336; color: white; font-size: 16px; border-radius: 8px;")
        self.layout.addWidget(self.undo_button)

        # Status log/Organized files display
        self.status_log = QTextEdit() # Keep QTextEdit for general messages
        self.status_log.setReadOnly(True)
        self.layout.addWidget(self.status_log)

        self.organized_files_table = QTableWidget()
        self.organized_files_table.setColumnCount(2)
        self.organized_files_table.setHorizontalHeaderLabels(["File Name", "Time Created"])
        self.organized_files_table.horizontalHeader().setStretchLastSection(True)
        self.organized_files_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.layout.addWidget(self.organized_files_table)

class SettingsDialog(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 600, 400)
        self.settings_manager = settings_manager
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.tab_widget = QTabWidget()
        self.general_tab = QWidget()
        self.duplicate_tab = QWidget()
        self.custom_rules_tab = QWidget()
        self.auto_cleanup_tab = QWidget()

        self.tab_widget.addTab(self.general_tab, "General")
        self.tab_widget.addTab(self.duplicate_tab, "Duplicate Handling")
        self.tab_widget.addTab(self.custom_rules_tab, "Custom Rules")
        self.tab_widget.addTab(self.auto_cleanup_tab, "Auto Cleanup")

        self.setup_general_tab()
        self.setup_duplicate_tab()
        self.setup_custom_rules_tab()
        self.setup_auto_cleanup_tab()

        main_layout.addWidget(self.tab_widget)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)

        self.load_settings()

    def setup_general_tab(self):
        layout = QFormLayout()
        self.general_tab.setLayout(layout)
        # Add custom sorting rules here later
        layout.addRow(QLabel("Custom Sorting Rules (Not yet implemented)"))

    def setup_duplicate_tab(self):
        layout = QFormLayout()
        self.duplicate_tab.setLayout(layout)

        self.skip_radio = QRadioButton("Skip")
        self.overwrite_radio = QRadioButton("Overwrite")
        self.rename_radio = QRadioButton("Rename")

        self.duplicate_group = QButtonGroup(self)
        self.duplicate_group.addButton(self.skip_radio)
        self.duplicate_group.addButton(self.overwrite_radio)
        self.duplicate_group.addButton(self.rename_radio)

        layout.addWidget(self.skip_radio)
        layout.addWidget(self.overwrite_radio)
        layout.addWidget(self.rename_radio)

    def setup_custom_rules_tab(self):
        layout = QVBoxLayout()
        self.custom_rules_list = QListWidget()
        layout.addWidget(self.custom_rules_list)

        add_rule_button = QPushButton("Add Rule")
        add_rule_button.clicked.connect(self.add_custom_rule)
        layout.addWidget(add_rule_button)

        self.custom_rules_tab.setLayout(layout)

    def add_custom_rule(self):
        # This will open another dialog to configure the rule
        rule_dialog = CustomRuleDialog(self)
        if rule_dialog.exec_():
            rule = rule_dialog.get_rule()
            if rule:
                self.settings_manager.settings["custom_rules"].append(rule)
                self.load_settings()

    def setup_auto_cleanup_tab(self):
        layout = QVBoxLayout()
        # Add widgets for auto-cleanup settings here
        self.auto_organize_interval_input = QLineEdit()
        self.auto_organize_interval_input.setPlaceholderText("Interval in minutes (0 for disabled)")
        layout.addWidget(QLabel("Auto Organize Interval (minutes):"))
        layout.addWidget(self.auto_organize_interval_input)
        self.auto_cleanup_tab.setLayout(layout)

    def load_settings(self):
        # General Tab
        # No general settings yet, but can be added here

        # Duplicate Handling Tab
        duplicate_handling = self.settings_manager.get_setting("duplicate_handling")
        if duplicate_handling == "skip":
            self.skip_radio.setChecked(True)
        elif duplicate_handling == "overwrite":
            self.overwrite_radio.setChecked(True)
        elif duplicate_handling == "rename":
            self.rename_radio.setChecked(True)

        # Custom Rules Tab
        self.custom_rules_list.clear()
        for rule in self.settings_manager.get_setting("custom_rules"):
            self.custom_rules_list.addItem(f"{rule['name']}: {rule['pattern']} -> {rule['destination']}")

        # Auto Cleanup Tab
        auto_organize_interval = self.settings_manager.get_setting("auto_organize_interval")
        self.auto_organize_interval_input.setText(str(auto_organize_interval))

    def save_settings(self):
        # Duplicate Handling Tab
        if self.skip_radio.isChecked():
            self.settings_manager.set_setting("duplicate_handling", "skip")
        elif self.overwrite_radio.isChecked():
            self.settings_manager.set_setting("duplicate_handling", "overwrite")
        elif self.rename_radio.isChecked():
            self.settings_manager.set_setting("duplicate_handling", "rename")

        # Custom Rules Tab - rules are saved directly when added/modified

        # Auto Cleanup Tab
        try:
            interval = int(self.auto_organize_interval_input.text())
            self.settings_manager.set_setting("auto_organize_interval", interval)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Auto organize interval must be a number.")

        self.settings_manager.save_settings()
        self.accept()


class CustomRuleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Custom Rule")
        self.rule = None

        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.rule_name_input = QLineEdit()
        self.pattern_input = QLineEdit()
        self.destination_input = QLineEdit()

        form_layout.addRow("Rule Name:", self.rule_name_input)
        form_layout.addRow("Pattern (e.g., .log, invoice_*.pdf):", self.pattern_input)
        form_layout.addRow("Destination Folder:", self.destination_input)

        layout.addLayout(form_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept_rule)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def accept_rule(self):
        name = self.rule_name_input.text().strip()
        pattern = self.pattern_input.text().strip()
        destination = self.destination_input.text().strip()

        if not name or not pattern or not destination:
            QMessageBox.warning(self, "Missing Information", "Please fill in all fields.")
            return

        self.rule = {"name": name, "pattern": pattern, "destination": destination}
        self.accept()

    def get_rule(self):
        return self.rule