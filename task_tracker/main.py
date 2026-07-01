import argparse
import json
from task_tracking import task_db

jsonfile = open('tasks.json', 'w')
json.dump(task_db, jsonfile)
jsonfile.close()

if not jsonfile:
    jsonfile = open('tasks.json', 'w')
    json.dump(task_db, jsonfile)
    jsonfile.close()
else:
    pass