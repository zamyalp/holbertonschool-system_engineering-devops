#!/usr/bin/python3
"""script that returns information about a given employee ID"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    file = id + ".json"
    users = {}
    list = []

    for task in todo:
        if task.get('userId') == int(id):
            Dict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.json().get("username")}
            list.append(Dict)
    users[id] = list

    with open(file, 'w') as result:
        json.dump(users, result)
