todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.\n")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(todo_list):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['task']} - {status}")

def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove.")
        return
    view_tasks()
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(todo_list):
        removed_task = todo_list.pop(task_number)
        print(f"Task '{removed_task['task']}' removed successfully.\n")
    else:
        print("Invalid task number.\n")


def mark_completed():
    if len(todo_list) == 0:
        print("No tasks to mark as completed.")
        return
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]["completed"] = True
        print(f"Task '{todo_list[task_number]['task']}' marked as completed.\n")
    else:
        print("Invalid task number.\n")

def menu():
    
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Mark completed")
    print("5. Exit")

    while(True): 
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")
menu()