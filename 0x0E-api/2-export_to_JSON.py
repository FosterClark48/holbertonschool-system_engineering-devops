#!/usr/bin/python3
"""
This script retrieves and displays the progress of a user's TODO list
from the JSONPlaceholder REST API and exports data in the JSON format.
"""
import requests
import sys
import json


if __name__ == '__main__':
    # Set the base URL for JSONPlaceholder REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Get user info using user ID provided as a CL arg
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()

    # Get the list of todos for the user
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    # Store format of tasks in tasks variable
    tasks = [{"task": t.get("title"), "completed": t.get("completed"),
              "username": user["username"]} for t in todos]

    # Store the tasks in a dictionary with the user ID as the key
    user_tasks = {sys.argv[1]: tasks}

    # Export the data to a JSON file
    with open('{}.json'.format(sys.argv[1]), 'w') as json_file:
        json.dump(user_tasks, json_file)
