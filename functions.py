FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list
    of todo_items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of todo_items into the
    text file
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)