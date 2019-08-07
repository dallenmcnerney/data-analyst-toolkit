import os
import utils


def list_files(parent_directory):
    file_list = []
    for path, dirs, files in os.walk(parent_directory):
        for file in files:
            file_list.append(os.path.join(path, file))
    return file_list


class FileInfo:

    def __init__(self, file_path):
        self.file_stats = os.stat(file_path)
        self.file_name = os.path.splitext(file_path)[1]
        self.create_date = utils.convert_time_to_date(self.file_stats.st_ctime)
        self.create_time = utils.convert_time_to_time(self.file_stats.st_ctime)
        self.modify_date = utils.convert_time_to_date(self.file_stats.st_mtime)
        self.modify_time = utils.convert_time_to_time(self.file_stats.st_mtime)
        self.size_in_megabytes = self.file_stats.st_size/1000


# TODO: Finish PBC log function


def pbc_log(path, output_name, file_type=None, delimiter='|', destination=None):
    print('Creating inventory list of the following directory and subdirectories:')
    print(''.join(path, '\n'))
    if '.' in output_name:
        output_file_type = output_name
    return output_name
