import shutil
import os

# Specify the directory path


def pur(directory_path):

    # Iterate through the contents of the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            # Check if the item is a file or a directory
            if os.path.isfile(file_path) or os.path.islink(file_path):
                # Remove the file
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # Recursively remove the directory and its contents
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
