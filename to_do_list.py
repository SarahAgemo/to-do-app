
tasks = []


def add_task():
    task = input("Add a task: ")
    tasks.append(task)
    print(f"Task '{task}' added")


def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("enter the # to delete: "))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed.")
        else:
            print(f"Task No. {task_to_delete} not found.")
    except:
        print("Invalid input.")


if __name__ == "__main__":
    # Create loop to run the app
    print("To-Do List")
    while True:
        print("\n")
        print("Options:")
        print("--------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Choose an action: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again")

    print("Goodbye")
