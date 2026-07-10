
import time
import datetime
import argparse
import json
import random
import string
import os
from pathlib import Path

TASK_FILE = Path(__file__).parent.parent / "tasks.json"
TASK_FILE.parent.mkdir(exist_ok=True)

if not TASK_FILE.exists():
    with open(TASK_FILE, "w") as f:
        json.dump([], f)

def add_task(task_description, status="todo"):
    with open(TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    timestamp = int(time.time())
    currentTime = datetime.datetime.fromtimestamp(timestamp)
    random_id = int(''.join(random.choices(string.digits, k=6)))
    task = {
        "id": random_id,
        "task": task_description,
        "status": status,
        "createdAt": str(currentTime),
        "updatedAt": str(currentTime)
    }
    task_db_temp.append(task)
    with open(TASK_FILE, "w") as file:
        json.dump(task_db_temp, file, indent=4)
    return task


def update_task(id, new_task):
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    timestamp = int(time.time())
    currentTime = datetime.datetime.fromtimestamp(timestamp)
    for task in task_db_temp:
        if task['id'] == id:
            task['task'] = new_task
            task['updatedAt'] = str(currentTime)
            with open(TASK_FILE, "w") as file:
                json.dump(task_db_temp, file, indent=4)
            return f"Updated task name for: {task['id']}, to: {task['task']}" 
    return "ID was not found"



def update_status(id, new_status):
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    timestamp = int(time.time())
    currentTime = datetime.datetime.fromtimestamp(timestamp)
    for task in task_db_temp:
        if task['id'] == id:
            task['status'] = new_status
            task['updatedAt'] = str(currentTime)
            with open(TASK_FILE, "w") as file:
                json.dump(task_db_temp, file, indent=4)
            return f"Updated status for task {task['id']} to: {task['status']}" 
    return "ID was not found"


def delete_task(id):
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    updated_tasks = [task for task in task_db_temp if task['id'] != id]
    if len(updated_tasks) == len(task_db_temp):
        return "ID was not found"
    with open(TASK_FILE, "w") as file:
        json.dump(updated_tasks, file, indent=4)
    return f"Task {id} has been deleted"

def list_tasks():
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    return task_db_temp

def list_tasks_todo():
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    return [i for i in task_db_temp if i['status'] == "todo"]

def list_tasks_inprogress():
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    return [i for i in task_db_temp if i['status'] == "in progress"]

def list_tasks_done():
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    return [i for i in task_db_temp if i['status'] == "done"]

def list_tasks_not_done():
    with open (TASK_FILE, "r") as f:
        task_db_temp = json.load(f)
    return [i for i in task_db_temp if not i['status'] == "done"]

        

    
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

parser_add = subparsers.add_parser("add")
parser_update_task = subparsers.add_parser("update-task")
parser_update_status = subparsers.add_parser("update-status")
parser_delete = subparsers.add_parser("delete-task")
parser_list_tasks = subparsers.add_parser("list-tasks")
parser_list_todo = subparsers.add_parser("list-todo")
parser_list_inprogress = subparsers.add_parser("list-inprogress")
parser_list_done = subparsers.add_parser("list-done")
parser_list_not_done = subparsers.add_parser("list-not-done")

parser_add.add_argument("task", nargs="?", default=None)

parser_update_task.add_argument("updateTaskID", type=int)
parser_update_task.add_argument("updateTaskName")

parser_update_status.add_argument("updateStatusID", type=int)
parser_update_status.add_argument("updateStatus")

parser_delete.add_argument("deleteTaskID", type=int)


args = parser.parse_args()


if args.command == "add":
    added_task = add_task(args.task)
    print(f"Task successfully added, ID: {added_task['id']}")
elif args.command == "update-task":
    print(update_task(args.updateTaskID, args.updateTaskName))
elif args.command == "update-status":
    print(update_status(args.updateStatusID, args.updateStatus))
elif args.command == "delete-task":
    result = delete_task(args.deleteTaskID)
    if not result:
        print("There are no tasks to be deleted.")
    else:
        print(result)
elif args.command == "list-tasks":
    result = list_tasks()
    if result:
        print(result)
    else:
        print("There are no tasks")
elif args.command == "list-todo":
    result = list_tasks_todo()
    if result:
        print(result)
    else:
        print("There are no tasks todo")
elif args.command == "list-inprogress":
    result = list_tasks_inprogress()
    if result:
        print(result)
    else:
        print("There are no tasks in progress")
elif args.command == "list-done":
    result = list_tasks_done()
    if result:
        print(result)
    else:
        print("No tasks are done")
elif args.command == "list-not-done":
    result = list_tasks_not_done()
    if result:
        print(result)
    else:
        print("All tasks are done")





       




