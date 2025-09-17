"""
cleanup_temp.py
Deletes files and folders inside a temporary directory.
"""

import os
import shutil


def clean_temp(folder: str = "C:/Temp") -> None:
    """
    Delete all files and subfolders inside the given folder.

    Args:
        folder (str): Path to the folder to clean.

    Returns:
        None
    """
    if not os.path.exists(folder):
        print(f"⚠️ Folder '{folder}' does not exist.")
        return

    deleted_count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            deleted_count += 1
        except Exception as e:
            print(f"⚠️ Could not delete '{file_path}': {e}")

    print(f"✅ Cleaned {deleted_count} items from '{folder}'.")


if __name__ == "__main__":
    clean_temp()
