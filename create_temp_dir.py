import os

try:
    os.makedirs('C:/Users/A R Khan/OneDrive/Documents/Trae/software/temp_next_app', exist_ok=True)
    print("Directory created successfully.")
except Exception as e:
    print(f"Error creating directory: {e}")