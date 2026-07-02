
import datetime
import argparse
import json

task_db = []
with open("tasks.json", "w") as f:
    json.dump(task_db, f)


def add_task(id, task, status):
    task_db.append({
        "id": id,
        "task": task,
        "status": status
    })
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


def update_task(id, new_task):
    for i in task_db:
        if i['id'] == id:
            i['task'] = new_task
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


def update_status(id, new_status):
    for i in task_db:
        if i['id'] == id:
            i['status'] = new_status
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)


def delete_task(id):
    for i in task_db:
        if i['id'] == id:
            task_db.remove(i)
            break
    with open("tasks.json", "w") as file:
        json.dump(task_db, file, indent=4)

add_task(1, 'eat chicken', 'in progress')
add_task(2, 'eat lamb', 'in progress')
            

