#!/usr/bin/python3
"""script that return information for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    users = requests.get(user).json()
    TODO = requests.get(todo).json()

    num_task_done = 0
    all = 0
    done = []

    for task in TODO:
        all += 1
        if task.get("completed") is True:
            num_task_done += 1
            done.append(task.get("title"))

    response = "Employee {} is done with tasks({}/{}):"
    print(response.format(users.get("name"), num_task_done, all))
    for task in done:
        print("\t {}".format(task))
