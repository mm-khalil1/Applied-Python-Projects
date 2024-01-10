"""
To Do List

This program allows users to manage tasks through a simple command-line interface.
Users can add tasks, view existing tasks, remove tasks, and exit the program.

Author: Mahmoud Khalil
Date: 07-12-2023
"""

def get_task():
    """
    Display a menu for the user to choose a task and return the selected choice as an integer.

    Choices:
    1 - Add a task
    2 - View tasks
    3 - Remove a task
    4 - Exit

    Returns:
    int: User-selected choice
    """
    print("\nChoose one of the following (from 1 to 4): ")
    return int(input("1-Add a task, 2-View tasks, 3-Remove a task, 4-Exit -> "))

def add_task(lst):
    """
    Prompt the user to input a task and add it to the given list.

    Args:
    lst (list): List to which the task will be added.

    Returns:
    list: Updated list after adding the task.
    """
    task = input("Type the task you want to add: ")
    lst.append(task)
    print("Task added successfully.")

def view_tasks(lst):
    """
    Display the tasks in the given list.

    Args:
    lst (list): List of tasks to be displayed.
    """
    if len(lst) == 0:
        print("There are no tasks.")
        return
    for i in range(0, len(lst)):
        print(f"Task {i + 1}: {lst[i]}")

def remove_task(lst):
    """
    Remove a task from the given list based on user input.

    Args:
    lst (list): List from which a task will be removed.
    """
    number_of_tasks = len(lst)
    if number_of_tasks == 0:
        print("There are no tasks to remove.")
        return

    print("Here are the tasks: ")
    view_tasks(lst)

    try:
        task_to_remove = int(input(f"Choose the task you would like to remove (from 1 to {number_of_tasks})? "))
    except ValueError:
        print("Invalid input.")
        return

    if task_to_remove not in range(1, number_of_tasks + 1):
        print("There is no such task.")
        return

    del lst[task_to_remove - 1]
    print(f"Task {task_to_remove} removed successfully.")

# Main program
lst = []
while True:
    choice = get_task()

    if choice == 1:
        add_task(lst)
    elif choice == 2:
        view_tasks(lst)
    elif choice == 3:
        remove_task(lst)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")
