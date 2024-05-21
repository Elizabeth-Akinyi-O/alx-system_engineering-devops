#!/usr/bin/python3
"""
Returns information about an employee's todo_list progress using REST API.
- Exports data in the CSV format.
- Records all tasks that are owned by this employee.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    empl_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + empl_id
    response = requests.get(user_url)
    user_name = response.json().get('username')
    task = user_url + '/todos'
    response = requests.get(task)
    todo_list = response.json()

    with open('{}.csv'.format(empl_id), 'w') as csvfile:
        for task in todo_list:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                empl_id, user_name, completed, title_task))
