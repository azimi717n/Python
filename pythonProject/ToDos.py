while True:
    user_action = input("\n\nType add, show, edit, complete or exit:\t")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            '''
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            '''
            ## below is better way by doing with context manger so now we don't need to close file
            ## because "with context manager" will take care of this

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            '''
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
            '''

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':  ## | is bitwise OR operator
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            #new_todos =  [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}-{item}")
        case 'edit':
            number = int( input("Number of todo to Edit:\t"))
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_to_do =input("Enter new to do: ")
            todos[number] = new_to_do + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            item_remove = eval(input("Enter number to remove:"))

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            index = item_remove - 1
            to_do_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {to_do_remove} was removed from the list"
            print(message)
        case 'exit' | '0':
            break

print("Bye!")








