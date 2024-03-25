#!/usr/bin/python3
"""making a REST API for todos of users"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = requests.get(url)
    user_name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for i in tasks:
        if i.get('completed'):
            done_tasks.append(i)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, done, len(tasks)))

    for i in done_tasks:
        print("\t {}".format(i.get('title')))
