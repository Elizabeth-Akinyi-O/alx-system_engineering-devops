#!/usr/bin/python3
"""
Returns information about an employee's todo_list progress using REST API.
- Export data in the JSON format.
- Records all tasks from all employees.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    Users = response.json()

    users_dict = {}
    for employee in Users:
        USER_ID = employee.get('id')
        USERNAME = employee.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        response = requests.get(url)

        todo_list = response.json()
        users_dict[USER_ID] = []
        for task in todo_list:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_dict, file)
