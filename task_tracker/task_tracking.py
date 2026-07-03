
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
    random_id = ''.join(random.choices(string.digits, k=6))
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
    if not any(i["id"] == id for i in task_db):
        print("ID was not found")
    else:
        for i in task_db:
            if i['id'] == id:
                i['task'] = new_task
        else:
            print("ID does not exist in task records")
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


def update_status(id, new_status):
    if not any(i["id"] == id for i in task_db):
        print("ID was not found")
    else:
        for i in task_db:
            if i['id'] == id:
                i['status'] = new_status
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


def delete_task(id):
    if not any(i["id"] == id for i in task_db):
        print("ID was not found")
    else:
        for task in task_db:
            if task['id'] == id:
                task_db.remove(task)
            break
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


        



parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

parser_add = subparsers.add_parser("add")
parser_add.add_argument("taskDescription")

args = parser.parse_args()

if args.taskDescription:
    result = add_task(args.taskDescription)
    print(f"Task successfully added, ID: {result['id']}")

       




