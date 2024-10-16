import json
import os

# TaskManager class handles all operations related to tasks.
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    # Add a new task with a title.
    def add_task(self, title):
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "title": title, "completed": False})
        print(f"Task '{title}' added successfully!")

    # Display all tasks with their status.
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{task['id']}: {task['title']} [{status}]")

    # Delete a task by its ID.
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        print(f"Task with ID {task_id} deleted.")

    # Mark a task as completed.
    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task with ID {task_id} marked as completed.")
                break
        else:
            print(f"No task found with ID {task_id}.")

    # Save tasks to a file named tasks.json.
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved to tasks.json.")

    # Load tasks from tasks.json if it exists.
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded from tasks.json.")
        else:
            print("No file named tasks.json found. Starting with an empty task list.")

# Command-line interface function to interact with the user.
def run_cli():
    manager = TaskManager()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                manager.mark_task_completed(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "5":
            manager.save_tasks()
        elif choice == "6":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_cli()
