#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    dictionary = {}

    for u in users:
        user_id = u.get('id')
        username = u.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for t in tasks:
            dictionary[user_id].append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dictionary, f)
