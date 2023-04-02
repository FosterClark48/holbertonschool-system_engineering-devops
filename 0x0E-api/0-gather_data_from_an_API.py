#!/usr/bin/python3
"""
This script retrieves and displays the progress of a user's TODO list
from the JSONPlaceholder REST API.
"""
import requests
import sys


if __name__ == '__main__':
    # Set the base URL for JSONPlaceholder REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Get user info using user ID provided as a CL arg
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()

    # Get the list of todos for the user
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    # Filter the list of todos to only include completed tasks
    completed = [O.get("title") for O in todos if O.get("completed") is True]

    # Display the user's progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print each completed task on a new line with a tab indent
    for task in completed:
        print("\t {}".format(task))
