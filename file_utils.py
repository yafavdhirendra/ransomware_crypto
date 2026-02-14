import os
from config import SKIP_DIRS, SKIP_FILES

def collect_files(folder):
    file_list = []

    for root, dirs, files in os.walk(folder):
        # Skip unwanted folders
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for f in files:
            # Skip python files and salt file
            if f.endswith(".py") or f in SKIP_FILES:
                continue

            file_list.append(os.path.join(root, f))

    return file_list
