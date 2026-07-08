
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
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    if not any(i["id"] == id for i in task_db_temp):
        print("ID was not found")
    else:
        for i in task_db_temp:
            if i['id'] == id:
                i['status'] = new_status
                task_db_temp.append(i)
    with open("tasks.json", "w") as file:
        json.dump(task_db_temp, file, indent=4)


def delete_task(id):
    with open ("tasks.json", "r") as f:
        task_db_temp = json.load(f)
    if not any(i["id"] == id for i in task_db_temp):
        print("ID was not found")
    else:
        for task in task_db_temp:
            if task['id'] == id:
                task_db_temp.remove(task)
            break
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


        
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

parser_add = subparsers.add_parser("add")
parser_update_task = subparsers.add_parser("update-task")
parser_update_status = subparsers.add_parser("update-status")
parser_delete = subparsers.add_parser("delete")

parser_add.add_argument("task", nargs="?", default=None)

parser_update_task.add_argument("updateTaskID", type=int)
parser_update_task.add_argument("updateTaskName")

parser_update_status.add_argument("--updateStatusID", type=int)

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
   
""" if updated_task == str:
        print(updated_task)
    else:
        print(f"Task successfully updated, ID: {updated_task['id']}") """



       




