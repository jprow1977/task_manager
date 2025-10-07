from functions import get_tasks, write_tasks
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:

    user_action = input("Type add, show, edit, complete or exit: ").strip()
    user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:]

        list_of_tasks = get_tasks()

        list_of_tasks.append(task + "\n")

        write_tasks(list_of_tasks)

    elif user_action.startswith('show'):

        list_of_tasks = get_tasks()

        for index, item in enumerate(list_of_tasks):
            print(f'{index + 1}-{item.strip()}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            new_task = input("Enter replacement task:")

            list_of_tasks = get_tasks()

            list_of_tasks[number] = new_task + "\n"

            write_tasks(list_of_tasks)

        except IndexError:
            print("There is not a item with that number. Please select again.")
            continue

        except ValueError:
            print('Not valid. Please enter a number.')
            continue

    elif user_action.startswith('complete'):
        try:
            task_to_remove = int(user_action[8:]) - 1

            list_of_tasks = get_tasks()

            list_of_tasks.pop(task_to_remove)

            write_tasks(list_of_tasks)
        except IndexError:
            print("There is no item with that number. Please select again.")
            continue

        except ValueError:
            print("Not a valid number. Please enter again.")
            continue
    elif user_action == 'exit':
        break

    else:
        print('Command is not valid.')











