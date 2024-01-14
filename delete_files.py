import os

def delete_temp_files():
    # List of folders to delete files from
    folders_to_clean = ["splited_video", "Temp_files", "audios"]

    for folder_name in folders_to_clean:

        # Get a list of all files in the folder
        files = os.listdir(folder_name)
        for file in files:
            file_path = os.path.join(folder_name, file)
            # Check if it's a file (not a directory) and delete it
            if os.path.isfile(file_path):
                os.remove(file_path)


delete_temp_files()