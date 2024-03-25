#!/usr/bin/python3
"""script to export data in the CSV format"""

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

    with open('{}.csv'.format(user_id), 'w') as f:
        for i in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(user_id, user_name, i.get('completed'),
                            i.get('title')))
