import json
import os

class SettingsManager:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = {
            "custom_rules": [],  # List of dictionaries, each representing a rule
            "duplicate_handling": "skip", # skip, overwrite, rename
            "auto_organize_interval": 0 # in minutes, 0 for disabled
        }
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        return {
            "custom_rules": {},
            "duplicate_handling": "rename", # or "skip", "overwrite"
            "auto_organize_interval": 0 # in hours, 0 for disabled
        }

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()