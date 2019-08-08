import pyperclip
from utils import row_string_to_list


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
