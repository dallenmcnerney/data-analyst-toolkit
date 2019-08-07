import pyperclip


def format_select_sql_columns(select_as=False):
    columns = pyperclip.paste()
    columns_list = columns.split('\n')
    output_string = ''
    for column in columns_list:
        if select_as:
            output_string += ''.join(('[', column, '] as [', column, '],\n'))
        else:
            output_string += ''.join(('[', column, '],\n'))
    output_string = output_string[:-2]
    pyperclip.copy(output_string)
    return output_string
