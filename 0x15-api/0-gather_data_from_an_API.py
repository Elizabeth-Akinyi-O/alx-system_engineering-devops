#!/usr/bin/python3
""" Returns information about an employee's todo_list progress using REST API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            """ Convert the employee ID to an integer """
            emp_id = int(sys.argv[1])
            """ GET request to fetch the user data in JSON format """
            req = requests.get('{}/users/{}'.format(REST_API, emp_id)).json()
            """ GET request to fetch all tasks """
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            empl_name = req.get('name')
            """ Filter tasks to include only those that belong to the user """
            tasks = list(filter(lambda x: x.get('userId') == emp_id, task_req))
            """ Filter tasks to include only those that are completed """
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            """ Print summary of tasks """
            print(
                'Employee {} is done with todo_list({}/{}):'.format(
                    empl_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            """ Print titles of completed tasks """
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
