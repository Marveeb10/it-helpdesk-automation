"""
batch_rename.py
Renames .txt files in a folder with a given prefix.
"""

import os


def batch_rename(folder: str, prefix: str) -> None:
    """
    Rename all .txt files in the given folder.

    Args:
        folder (str): Folder containing files to rename.
        prefix (str): Prefix to apply to renamed files.

    Returns:
        None
    """
    if not os.path.exists(folder):
        print(f"⚠️ Folder '{folder}' not found.")
        return

    count = 0
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            count += 1
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, f"{prefix}_{count}.txt")
            os.rename(src, dst)

    print(f"✅ Renamed {count} files in '{folder}'.")


if __name__ == "__main__":
    # Example usage
    batch_rename("C:/Users/Marvee/Documents/test_files", "log")
