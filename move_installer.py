import shutil
import os

source_path = r'C:\Users\A R Khan\OneDrive\Documents\Trae\software\FileManagementSoftware_Installer.exe'
destination_path = r'C:\Users\A R Khan\OneDrive\Documents\Trae\software\landing-page\public\FileManagementSoftware_Installer.exe'

try:
    shutil.move(source_path, destination_path)
    print(f"Successfully moved {source_path} to {destination_path}")
except FileNotFoundError:
    print(f"Error: Source file not found at {source_path}")
except Exception as e:
    print(f"An error occurred: {e}")
