#!/usr/bin/python3
"""For a given employee ID, returns his/her TODO list progress"""
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if isinstance(id, int):
            user_resp = requests.get("{}/users/{}".format(url, id)).json()
            todos_resp = requests.get("{}/todos".format(url)).json()
            user_name = user_resp.get('name')
            todos = [todo for todo in todos_resp if todo.get('userId') == id]
            complete_todo = [todo for todo in todos if todo.get('completed')]

            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                            '"{}", "{}","{}","{}"\n'.format(
                                id,
                                user_name,
                                todo.get('completed'),
                                todo.get('title')
                                )
                            )
