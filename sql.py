import pyperclip
from utils import row_string_to_list
import re


def sql_columns_to_select(select_as=False):
    columns = pyperclip.paste()
    columns_list = row_string_to_list(columns)
    if columns_list[-1] == '':
        columns_list.pop(-1)
    output_string = ''
    for column in columns_list:
        if select_as:
            output_string += ''.join(('[', column, '] as [', column, '],\n'))
        else:
            output_string += ''.join(('[', column, '],\n'))
    output_string = output_string[:-2]
    pyperclip.copy(output_string)
    return output_string


def trim_sql_columns():
    columns = pyperclip.paste()
    columns_list = row_string_to_list(columns)
    if columns_list[-1] == '':
        columns_list.pop(-1)
    output_string = ''
    for column in columns_list:
        output_string += ''.join(('LTRIM(RTRIM([', column, '])) as [', column, '],\n'))
    output_string = output_string[:-2]
    pyperclip.copy(output_string)
    return output_string


# TODO: Add functionality for temp tables


def identify_used_sql_tables(script_location):
    with open(script_location, 'r') as sql_file:
        file_text = sql_file.read()
        parsed_data = re.findall(r'(from\s+|FROM\s+)(\n*)(dbo\.|DBO\.|\[dbo\]\.|\[DBO\]\.)*(\[*\w+\]*)', file_text)
        table_list = []
        for data in parsed_data:
            table_list.append(data[-1].replace('[', '').replace(']', ''))
        return table_list


def identify_created_sql_tables(script_location):
    with open(script_location, 'r') as sql_file:
        file_text = sql_file.read()
        parsed_data = re.findall(r'(into\s+|INTO\s+)(\n*)(dbo\.|DBO\.|\[dbo\]\.|\[DBO\]\.)*(\[*\w+\]*)', file_text)
        table_list = []
        for data in parsed_data:
            table_list.append(data[-1].replace('[', '').replace(']', ''))
        return table_list

