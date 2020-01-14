TO DO API
=================

This api allows create users and tasks. The api contains the follow endpoints.
- /users
    - GET method -> list all the users
    - POST method -> create a new user
- /users/<id_user>
    - GET method -> retrieve the user data
    - PUT method -> update the user data
    - DELETE method -> delete the user
- /tasks
    - GET method --> list all the tasks
    - POST method --> create a new task
- /tasks/<id_task>
    - GET method -> retrieve the task data
    - PUT method -> update the task data
    - DELETE method -> delete the task
- /tasks/user/<id_user>
    - GET method -> list all tasks of a user
    
    
## Building

It is needed the python3 library installed.

It is best to use the python `virtualenv` tool to build locally:

```sh
$ sudo apt-get install python3.6
$ sudo apt-get install virtualenv
$ sudo apt-get install python3-pip
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. 
