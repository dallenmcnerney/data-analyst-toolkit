import os


def inventory(parent_directory):
    for path, dirs, files in os.walk(parent_directory):
        for file in files:
            return os.path.join(path, file)

