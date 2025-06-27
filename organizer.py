import os
import shutil
import time
from datetime import datetime
import re

from file_manager import FileManager
from settings import SettingsManager

class FileOrganizer:
    def __init__(self):
        self.file_manager = FileManager()
        self.settings_manager = SettingsManager()
        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Executables": [".exe", ".dmg", ".app", ".deb", ".rpm"],
            "Other": [] # Catch-all for uncategorized files
        }
        self.last_moved_files = []
        self.undo_stack = [] # Initialize undo stack

    def organize_folder(self, source_folder):
        self.last_moved_files = [] # Clear previous undo history
        if not os.path.isdir(source_folder):
            return "Error: Source folder does not exist.", []

        moved_files_info = []
        files_to_organize = self.file_manager.get_files_in_folder(source_folder)
        duplicate_handling = self.settings_manager.get_setting("duplicate_handling")
        custom_rules = self.settings_manager.get_setting("custom_rules")

        for item_path in files_to_organize:
            item_name = os.path.basename(item_path)
            
            # Apply custom rules first
            destination_folder_name = None
            for rule in custom_rules:
                if self._match_custom_rule(item_name, rule['pattern']):
                    destination_folder_name = rule['destination']
                    break
            
            if destination_folder_name is None:
                # Fallback to default categorization if no custom rule matches
                file_extension = self.file_manager.get_file_extension(item_name)
                destination_folder_name = self._get_destination_folder(file_extension)
            
            destination_path = os.path.join(source_folder, destination_folder_name)
            success, msg = self.file_manager.create_directory(destination_path)
            if not success:
                self.undo_stack.append({'type': 'log', 'message': msg})
                continue
            
            original_source_path = item_path
            final_destination_file_path = os.path.join(destination_path, item_name)
            
            if os.path.exists(final_destination_file_path):
                if duplicate_handling == "skip":
                    self.undo_stack.append({'type': 'log', 'message': f"Skipped: {item_name} (duplicate)"})
                    continue
                elif duplicate_handling == "overwrite":
                    os.remove(final_destination_file_path)
                    self.undo_stack.append({'type': 'log', 'message': f"Overwritten: {item_name}"})
                elif duplicate_handling == "rename":
                    base, ext = os.path.splitext(item_name)
                    i = 1
                    while os.path.exists(os.path.join(destination_path, f"{base}({i}){ext}")):
                        i += 1
                    final_destination_file_path = os.path.join(destination_path, f"{base}({i}){ext}")
                    self.undo_stack.append({'type': 'log', 'message': f"Renamed and moved: {item_name} to {os.path.basename(final_destination_file_path)}"})

            success, msg = self.file_manager.move_file(original_source_path, final_destination_file_path)
            self.undo_stack.append({'type': 'log', 'message': msg})
            if success:
                # Get creation time of the moved file
                creation_time = os.path.getctime(final_destination_file_path)
                moved_files_info.append({
                    'file_name': os.path.basename(final_destination_file_path),
                    'time_created': datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                })
                self.undo_stack.append({
                    'type': 'move',
                    'source': original_source_path,
                    'destination': final_destination_file_path,
                    'timestamp': time.time()
                })

        return f"Organization complete. Moved {len(moved_files_info)} files.", moved_files_info

    def undo_last_organization(self):
        if not self.undo_stack:
            return "No operations to undo.", []

        # Filter out only 'move' operations for undo
        moves_to_undo = [item for item in self.undo_stack if item['type'] == 'move']
        if not moves_to_undo:
            return "No move operations to undo.", []

        # Iterate in reverse to undo in the correct order
        undo_log_entries = []
        for move_info in reversed(moves_to_undo):
            original_source = move_info["source"]
            current_destination = move_info["destination"]
            
            if os.path.exists(current_destination):
                try:
                    shutil.move(current_destination, original_source)
                    undo_log_entries.append(f"Undid: Moved {os.path.basename(current_destination)} back to {os.path.dirname(original_source)}")
                except Exception as e:
                    undo_log_entries.append(f"Error undoing move for {os.path.basename(current_destination)}: {e}")
            else:
                undo_log_entries.append(f"Warning: {os.path.basename(current_destination)} not found for undo.")
        
        # Clear the undo stack after performing undo
        self.undo_stack = []

        # Return the log entries for display
        return "Undo complete.", undo_log_entries

    def _match_custom_rule(self, filename, pattern):
        # Simple matching for now: checks if pattern is in filename or is an extension
        # Can be expanded for regex or more complex patterns
        if pattern.startswith('.'):
            return filename.lower().endswith(pattern.lower())
        else:
            return pattern.lower() in filename.lower()

    def _get_destination_folder(self, extension):
        for category, extensions in self.categories.items():
            if extension in extensions:
                return category
        return "Other"