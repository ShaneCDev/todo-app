FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items
    :param filepath:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write to-do items in the text file
    :param todos_arg:
    :param filepath:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
