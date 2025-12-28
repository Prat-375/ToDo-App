import functions
import time

now =time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # add a new task to the todos list in todos txt file
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # show tasks in the todos list
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            # update an existing task with a new task
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a todo to update the existing todo with: ")
            todos[number] = new_todo + '\n'

        except ValueError:
            print("You entered an invalid command. Please try again!")
            continue

        except IndexError:
            print("There is no item with that number")
            continue

        functions.write_todos(todos)

    elif user_action.startswith('complete'):
        # when task is completed, remove it from the todos list
        try:
            todos = functions.get_todos()

            to_remove = int(user_action[9:])
            index = to_remove - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"{index + 1}-{todo_to_remove} task removed")

        except IndexError:
            print("There is no item with that number")
            continue

        except ValueError:
            print("You entered an invalid command. Please try again!")
            continue

    elif user_action.startswith('exit'):
        # when operations are done, exit the program
        break

    else:
        # when anything other than cases are passed by user, a message is displayed to try input again
        print("You entered an unknown command. Please try again!")

print("Bye!")