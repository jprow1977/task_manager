def get_tasks(filepath='tasks.txt'):
    """read a text file and return as list of tasks."""
    with open(filepath, "r") as file_local:
        list_of_tasks_local = file_local.readlines()
    return list_of_tasks_local


def write_tasks(list_of_tasks_arg, filepath='tasks.txt'):
    """write a list of tasks to a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(list_of_tasks_arg)


print(__name__)

if __name__ == "__main__":
    print("hello from functions")
