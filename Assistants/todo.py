import json
import os

TODO_FILE = "data/todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TODO_FILE, 'w')as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return "Task added successfully"

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        return "No tasks yet"
    return "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))