#!/usr/bin/python3
"""
Returns information about an employee's todo_list progress using REST API.
- Exports data in the JSON format.
- Records all tasks that are owned by this employee.
"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    response = requests.get(user_url)
    USERNAME = response.json().get('username')
    task_url = user_url + '/todos'
    response = requests.get(task_url)
    todo_list = response.json()

    user_tasks = {USER_ID: []}

    for task in todo_list:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        user_tasks[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})

    """print(user_tasks)"""
    with open('{}.json'.format(USER_ID), 'w') as file:
        json.dump(user_tasks, file)
