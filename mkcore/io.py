import os


def list_files_in_path(path):
    files = []

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))

    return files
