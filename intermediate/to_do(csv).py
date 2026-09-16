"""
Command-Line To-Do List Application(CSV version)
-------------------------------------------------
Features:

- Add tasks 
- View tasks(with status:pending/done)
- Delete tasks 
- Mark tasks as completed
- Persistent storage using CSV file
- Basic error handling dfor invalid input and missing tasks 
"""

import csv
import os 
from datetime import datetime

DATA_FILE= "tasks.csv"
FIELDNAMES=["id","description","done","created_at"]

def load_tasks():
    """
      Load tasks from the CSV file . returns an empty list if the file does'nt exist or is corrupted. 
    """
    if not os.path.exists(DATA_FILE):
        return[]
    tasks = []
    try:
        with open(DATA_FILE,"r",newline="",encoding="utf-8")as f:
            reader= csv.DictReader(f)
            for row in reader:
                try:
                    tasks.append({
                        "id": int(row["id"]),
                        "description": row["description"],
                        "done": row["done"]=="True",
                        "created_at":row["created_at"],
                    })
                except(KeyError,ValueError):
                    continue 
    except OSError as e:
        print(f"⚠️ Warning: Could not read {DATA_FILE}({e}). Starting fresh.")
        return[]
    
    return tasks 

def save_tasks(tasks):
    """ Save the tasks list to the CSV file """
    try:
        with open(DATA_FILE,"w",newline="",encoding="utf-8")as f:
            writer = csv.DictWriter(f,fieldnames=FIELDNAMES)
            for task in tasks:
                writer.writerow(task)
    except OSError as e:
        print(f"error: Could not save the  tasks to file ({e}).")


def get_next_id(tasks):
            """"Generate the next available task ID."""
            if not tasks:
                return 1
            return max(task ["id"] for task in tasks)+1
                                         
# ---------------------Core Features-----------------

def add_task(tasks):
    description = input("Enter task description:").strip()

    if not description:
        print("Error: Task description cannot be empty.\n")
        return

    task={
        "id": get_next_id(tasks),
        "description": description ,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully!(ID{task['id']}).\n")

def view_tasks(tasks):
    if not tasks:
        print("No Task found. Your list is empty.\n")
        return
    
    print("\n" + "-" * 50)
    print(f"{'ID':<5}{'Status':<10}{'Description':<25}{'Created'}")
    print("-" * 50)
    for task in tasks:
        status = "✔ Done" if task["done"] else "⏳ Pending"
        print(f"{task['id']:<5}{status:<10}{task['description']:<25}{task['created_at']}")
    print("-" * 50 + "\n")


def find_task_by_id(tasks,task_id):
    for task in tasks:
        if task["id"]==task_id:
            return task
        return None
    
def get_valid_task_id(prompt="Enter task ID:"):
    raw=input(prompt).strip()
    if not raw.isdigit():
        print("Error:Please enter a valid task ID\n")
        return None
    return int(raw)

def delete_task(tasks):
    if not tasks:
        print("No task to delete.")
        return
    
    task_id=get_valid_task_id("Enter task ID to delete:")
    if task_id is None:
        return
    
    task= find_task_by_id(tasks,task_id)
    if task_id is None:
        return
    
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.\n")

def mark_done(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    task_id=get_valid_task_id("Enter task ID to update:")
    if task_id is None:
        return
    
    task= find_task_by_id(tasks,task_id)
    if task_id is None:
        print(f"Error:No task found with ID{task_id}.")
        return
    
    if task["done"]:
        print(f"Tassk{task_id}is already marked as done.")
        return
    task["done"]=True
    save_tasks(tasks)
    print(f"Task{task_id} marked as done.\n")




# ---------------------Main Menu-----------------------

MENU=""""
========== TO-DO LIST APP(CSV) ==========
1. Add Task
2. View Task
3. Mark Task as Done
4. Delete Task
5. Exit

====================
"""

def main():
    tasks=load_tasks()

    while True:
        print(MENU)
        choice=input("Choose an option(1-5):").strip()

        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            mark_done(tasks)
        elif choice=="4":
            delete_task(tasks)
        elif choice=="5":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Error: Invalid choice . Please select a valid number from(1-5)\n")


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting safely-your tasks are saved. ")

 
    

