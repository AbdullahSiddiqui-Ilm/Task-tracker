task_db = []

def __init__(self):
    pass

def add_task(id, task, status):
    task_db.append({
        "id": id,
        "task": task,
        "status": status
    })

def update_task(id, new_task):
    for i in task_db:
        if i['id'] == id:
            i['task'] = new_task
    return task_db

def delete_task(id):
    for i in task_db:
        if i['id'] == id:
            task_db.remove(i)
            break
    return task_db

add_task(1, 'eat chicken', 'in progress')
add_task(2, 'eat lamb', 'in progress')

print(delete_task(2))
            

