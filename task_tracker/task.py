
import datetime
import argparse
import json
import random
import string
import os

task_db =[]

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as f:
        json.dump(task_db, f)


def add_task(task_description, status="todo"):
    with open("tasks.json", "r") as f:
        task_db_temp = json.load(f)  
    random_id = int(''.join(random.choices(string.digits, k=6)))
    task = {
        "id": random_id,
        "task": task_description,
        "status": status
    }
    task_db_temp.append(task)
    with open("tasks.json", "w") as file:
        json.dump(task_db_temp, file, indent=4)
    return task


def update_task(id, new_task):
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    if not any(i["id"] == id for i in task_db_temp):
        return "ID was not found"
    else:
        for i in task_db_temp:
            if i['id'] == id:
                i['task'] = new_task
    with open("tasks.json", "w") as file:
        json.dump(task_db_temp, file, indent=4)
    return i



def update_status(id, new_status):
    new_status.lower()
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    if not any(i["id"] == id for i in task_db_temp):
        return "ID was not found"
    else:
        for i in task_db_temp:
            if i['id'] == id:
                i['status'] = new_status
                return i
    with open("tasks.json", "w") as file:
        json.dump(task_db_temp, file, indent=4)


def delete_task(id):
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    if not any(i["id"] == id for i in task_db_temp):
        return "ID was not found"
    else:
        for task in task_db_temp:
            if task['id'] == id:
                task_db_temp.remove(task)
    with open("tasks.json", "w") as file:
        json.dump(task_db_temp, file, indent=4)
    return task

def list_tasks():
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    for i in task_db_temp:
        print(i)
    return

def list_tasks_todo():
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    for i in task_db_temp:
        if i['status'] == "todo":
            print(i)
    return

def list_tasks_inprogress():
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    for i in task_db_temp:
        if i['status'] == "in progress":
            print(i)
    return

def list_tasks_done():
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    for i in task_db_temp:
        if i['status'] == "done":
            print(i)
    return

def list_tasks__not_done():
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    for i in task_db_temp:
        if not i['status'] == "done":
            print(i)
    return

    
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
parser_delete.add_argument("--deleteTask")


args = parser.parse_args()


if args.command == "add":
    added_task = add_task(args.task)
    print(f"Task successfully added, ID: {added_task['id']}")
elif args.command == "update-task":
    updated_task = update_task(args.updateTaskID, args.updateTaskName)
    if updated_task == str:
        print(updated_task)
    else:
        print(f"Task auccessfully updated, ID {updated_task['id']}")
elif args.command == "update-status":
    updated_status = update_status(args.updateStatusID, args.updateStatus)
    if updated_status == str:
        print(updated_status)
    elif updated_status['status'] == "in progress":
        print(update_status)
        print(f"Updated status for task {updated_status['id']} to: {updated_status['status']}")
    elif updated_status['status'] == "done":
        print(f"Updated status for task {updated_status['id']} to: {updated_status['status']}")
elif args.command == "delete-task":
    deleted_task = delete_task(args.deleteTaskID)
    if deleted_task == str:
        print(deleted_task)
    elif not deleted_task:
        print("There are no tasks to be deleted.")
    else:
        print(f"Task {deleted_task['id']} has been deleted")
elif args.command == "list-tasks":
    list_tasks()
elif args.command == "list-todo":
    list_tasks_todo()
elif args.command == "list-inprogress":
    list_tasks_inprogress()
elif args.command == "list-done":
    list_tasks_done()
elif args.command == "list-not-done":
    list_tasks_done()





       




