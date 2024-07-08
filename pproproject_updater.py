import os
import pyautogui
import time

def update_premiere_project(file_path):
    # Open Adobe Premiere Pro 2022 or Whatever versions you's gots 
    os.startfile("C:\\Program Files\\Adobe\\Adobe Premiere Pro 2022\\Adobe Premiere Pro.exe")
    
    # Wait for Premiere to open
    time.sleep(30)
    
    # Open the project file
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(2)
    pyautogui.typewrite(file_path)
    time.sleep(2)
    pyautogui.press('enter')
    
    # Wait for the project to load
    time.sleep(60)
    
    # Save the project
    pyautogui.hotkey('ctrl', 's')
    
    # Wait for the save to complete
    time.sleep(5)
    
    # Close Adobe Premiere Pro
    pyautogui.hotkey('alt', 'f4')
    time.sleep(10)

def main():
    project_directory = "path_to_your_projects"
    
    # Get a list of all project files in the directory
    project_files = [f for f in os.listdir(project_directory) if f.endswith('.prproj')]
    
    for project_file in project_files:
        file_path = os.path.join(project_directory, project_file)
        update_premiere_project(file_path)
        print(f"Updated {project_file} to Adobe Premiere Pro 2022")

if __name__ == "__main__":
    main()
