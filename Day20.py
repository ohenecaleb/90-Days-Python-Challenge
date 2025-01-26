import os
import shutil

def organize_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print(f"The folder path {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            target_folder = os.path.join(folder_path, file_extension.upper() + "Files")

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files_by_extension(folder_path)