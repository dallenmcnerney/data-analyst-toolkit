from datetime import datetime as dt
import os
import re
import faker
import pandas as pd
import itertools
import time
import shutil

'''Stopwatch class
Creates a stopwatch object. Has split and total functionality.
Example usage: 
st = Stopwatch()
st.start
st.split()
st.last
st.start
st.total()
'''


class Stopwatch:
    def __init__(self):
        self.__start_time = dt.now()
        self.__last_time = self.__start_time
        self.start = self.__time_text(self.__start_time)
        self.last = self.__time_text(self.__last_time)

    @staticmethod
    def __time_text(time):
        return dt.strftime(time, '%m/%d/%Y %H:%M:%S')

    @staticmethod
    def __time_difference_text(td):
        days, hours, minutes, seconds = td.days, td.seconds // 3600, (td.seconds % 3600) // 60, (td.seconds % 60)
        day_text = hours_text = minutes_text = seconds_text = ''
        if days > 0:
            day_text = ('%s day(s) ' % days)
        if hours > 0:
            hours_text = ('%s hour(s) ' % hours)
        if minutes > 0:
            minutes_text = ('%s minute(s) ' % minutes)
        if seconds > 0:
            seconds_text = ('%s second(s) ' % seconds)
        return ''.join([day_text, hours_text, minutes_text, seconds_text]).strip()

    @staticmethod
    def __time_diff(prev_time):
        current_time = dt.now()
        time_diff = current_time - prev_time
        return current_time, time_diff

    def split(self):
        current_time, time_diff = self.__time_diff(self.__last_time)
        self.__last_time = current_time
        self.last = self.__time_text(self.__last_time)
        print(self.__time_difference_text(time_diff))

    def total(self):
        current_time, time_diff = self.__time_diff(self.__start_time)
        print(self.__time_difference_text(time_diff))


'''TestData class
Creates a TestData object that generates random data such as name, phone number, address, date, etc. This 
object can be used to test other functions and classes
data = TestData(rows=100, fields=5)
pd = data.to_dataframe()
data.to_csv(sep=',')
'''

# TODO: Add additional potential fields


class TestData:
    def __init__(self, local='en_US', rows=100, fields=5):
        self.generator = faker.Faker(local)
        self.data = []
        self.__generate_data(rows=rows, fields=fields)

    def __generate_data(self, rows, fields):
        if fields > 5:
            print('Max 5 fields allowed')
            fields = 5
        self.fields = ['name', 'phone_number', 'address', 'date', 'city'][:fields]
        for i in range(rows):
            data_row = {}
            for field in self.fields:
                data_row[field] = eval(''.join(('self.generator.', field, '()'))).replace('\n', ' ')
            self.data.append(data_row)

    def to_dataframe(self):
        return pd.DataFrame(self.data)

    def to_csv(self, filename, destination=None, sep='|'):
        data = pd.DataFrame(self.data)
        if destination is None:
            destination = os.getcwd()
        data.to_csv(os.path.join(destination, filename), sep=sep, index=False)


def find_separators(string):
    separators = re.findall(r'\W', string)
    likely_separator = max(separators, key=separators.count)
    return likely_separator


# TODO: Identify optimal number of lines to write


def change_text_file_delimiter(filepath, new_file_name, destination=None, old_separator=None, new_separator='|'):
    if destination is None:
        destination = os.getcwd()
    new_lines = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            if not old_separator:
                old_separator = find_separators(line)
                print('No separator given, assuming %s is the separator' % old_separator)
                new_lines.append(line.replace(old_separator, new_separator))
            else:
                new_lines.append(line.replace(old_separator, new_separator))
    with open(os.path.join(destination, new_file_name), 'w+') as file:
        for line in new_lines:
            file.write(line)

# TODO: Create combine file


def read_n_lines(file, n=10):
    with open("datafile") as file:
        head = [next(file) for x in range(10)]
    print(head)


def delimit(delimiter, data, *args):
    args = [y for x in args for y in x]
    data = list(itertools.chain(data, args))
    data = [str(i) for i in data]
    return delimiter.join(data)


def output_data(data, output_name, file_type='.txt', destination=None, header=None):
    if destination is None:
        destination = os.getcwd()
    output_file = os.path.join(destination, output_name + file_type)
    if header is not None:
        data.insert(0, header)
    if file_type != '.txt':
        print('Non-text files to come. Switching to default .txt')
    with open(output_file, 'w+') as text_file:
        for row in data:
            text_file.write(''.join(row, '\n'))
    print(''.join("Output saved as '", output_name, file_type, "'"))
    print(''.join("In the following directory:"))
    print(''.join(destination, '\n'))


def convert_time_to_date(input_time):
    return time.strftime('%m/%d/%Y', time.gmtime(input_time))


def convert_time_to_time(input_time):
    return time.strftime('%H:%M:%S', time.localtime(input_time))


def row_string_to_list(rows):
    if '\r\n' in rows:
        split_list = rows.split('\r\n')
    elif '\r' in rows and '\n' not in rows:
        split_list = rows.split('\r')
    elif '\n' in rows and '\r' not in rows:
        split_list = rows.split('\n')
    try:
        if split_list[-1] == '':
            split_list.pop(-1)
        return split_list
    except (NameError, UnboundLocalError):
        print('No valid row delimiter')
        return None

# TODO: Add option to maintain subfolders


def move_files(files_list, output_folder, maintain_subfolders=False):
    if not maintain_subfolders:
        for file in files_list:
            shutil.copy2(file, output_folder)
