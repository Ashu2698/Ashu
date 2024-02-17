import os
import shutil

def organize_files(source_folder):
    # Create directories for different file types
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac'],
        'Others': []  # For all other file types
    }

    for dir_name in file_types.keys():
        os.makedirs(os.path.join(source_folder, dir_name), exist_ok=True)

    # Move files to appropriate directories
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(os.path.join(source_folder, filename), os.path.join(source_folder, category, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(os.path.join(source_folder, filename), os.path.join(source_folder, 'Others', filename))

def main():
    source_folder = input("Enter the path to the folder you want to organize: ")
    organize_files(source_folder)
    print("Files organized successfully.")

if __name__ == "__main__":
    main()
