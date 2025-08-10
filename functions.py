def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todo_local, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todo_local)
