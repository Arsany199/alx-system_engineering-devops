#!/usr/bin/python3
"""export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = requests.get(url)
    user_name = response.json().get('username')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {user_id: []}
    for i in tasks:
        dictionary[user_id].append({
            "task": i.get('title'),
            "completed": i.get('completed'),
            "username": user_name
        })
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(dictionary, f)
