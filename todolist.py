import os

# Initialize an empty to-do list
todo_list = {}

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. Update a task")
    print("3. View all tasks")
    print("4. Mark task as completed")
    print("5. Delete a task")
    print("6. Exit")

def add_task():
    task = input("Enter the new task: ")
    todo_list[task] = "Pending"
    print(f"Task '{task}' added.")

def update_task():
    task = input("Enter the task to update: ")
    if task in todo_list:
        new_task = input("Enter the updated task: ")
        todo_list[new_task] = todo_list.pop(task)
        print(f"Task '{task}' updated to '{new_task}'.")
    else:
        print("Task not found.")

def view_tasks():
    if todo_list:
        print("\nCurrent To-Do List:")
        for task, status in todo_list.items():
            print(f"Task: {task}, Status: {status}")
    else:
        print("Your to-do list is empty.")

def mark_task_completed():
    task = input("Enter the task to mark as completed: ")
    if task in todo_list:
        todo_list[task] = "Completed"
        print(f"Task '{task}' marked as completed.")
    else:
        print("Task not found.")

def delete_task():
    task = input("Enter the task to delete: ")
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' deleted.")
    else:
        print("Task not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            update_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
