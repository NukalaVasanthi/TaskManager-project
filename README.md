# Task Manager CLI Application

## Project Description
The **Task Manager CLI Application** is a Python-based command-line tool that helps users manage their tasks directly from the terminal. It supports adding, viewing, deleting, and marking tasks as completed. Tasks are saved to a file for persistence, so users can pick up where they left off.

## Features
- **Add a Task**: Create a new task by providing a title. Each task is assigned a unique ID.
- **View Tasks**: List all tasks with their IDs and completion status (completed or not).
- **Delete a Task**: Remove a task from the list by specifying its ID.
- **Mark a Task as Completed**: Change a task’s status to indicate it is finished.
- **Save and Load Tasks**: Tasks are saved to `tasks.json` for persistence and are automatically loaded when the application starts.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Getting Started

### Step 1: Clone or Download the Project
Download the project files or clone the repository using:
```bash
git clone <repository-url>
python task_manager.py
After running the script, you will see the following menu:
Task Manager CLI
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Save Tasks
6. Exit
Enter the number corresponding to the action you want to perform and follow the prompts. For example:
Task Manager CLI
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Save Tasks
6. Exit
Enter your choice: 1
Enter task title: Buy groceries
Task 'Buy groceries' added successfully!

Task Manager CLI
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Save Tasks
6. Exit
Enter your choice: 2
1: Buy groceries [Not Completed]
"# TaskManager-project" 
