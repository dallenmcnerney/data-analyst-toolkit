import os


def inventory(parent_directory):
    file_list = []
    for path, dirs, files in os.walk(parent_directory):
        for file in files:
            file_list.append(os.path.join(path, file))
    return file_list

