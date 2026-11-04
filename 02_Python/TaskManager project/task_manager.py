task = []

def add_task():
    title = input("Enter task title: ")

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)

    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. {task['title']} - {status}")

def main():
    while True:
        print("\n==== Task Manager ====")
        print('1. Add Task')
        print('2. Show Tasks')
        print('3. Complete Task')
        print('4. Delete Task')
        print('5. Exit')

        choice = input("Choose an option")

        if choice == '1':
            print("Add task selected")
            add_task()

        elif choice == '2':
            print("Show tasks selected")
            show_tasks()

        elif choice == '3':
            print("Complete task selected")

        elif choice == '4':
            print("Delete task selected")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    maim()