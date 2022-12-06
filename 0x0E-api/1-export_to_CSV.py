#!/usr/bin/python3
"""script that returns information about a given employee ID"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    name = user.json().get("username")
    file = id + ".csv"

    with open(file, 'w') as result:
        write = csv.writer(result,
                           delimiter=",",
                           quotechar='"',
                           quoting=csv.QUOTE_ALL,
                           lineterminator='\n')
        for task in todo.json():
            if task.get('userId') == int(id):
                write.writerow([id,
                                name,
                                str(task.get("completed")),
                                task.get("title")])
