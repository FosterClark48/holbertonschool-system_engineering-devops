#!/usr/bin/python3
"""
This script retrieves and displays the progress of a user's TODO list
from the JSONPlaceholder REST API and exports the data in JSON format.
"""
import requests
import json


if __name__ == '__main__':
    # Set the base URL for JSONPlaceholder REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Get list of users
    users = requests.get(url + 'users').json()

    # Initialize an empty dictionary to store todo data for all employees
    all_todos = {}

    # Iterate through the list of users
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get the list of todos for the user
        todos = requests.get(url + 'todos', params={"userId": user_id}).json()

        # Store todo data in the requried format
        all_todos[user_id] = [{"username": username,
                               "task": todo.get("title"),
                               "completed": todo.get("completed")}
                              for todo in todos]

    # Save the data to a JSON file name 'todo_all_emplyees.json'
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_todos, json_file)
