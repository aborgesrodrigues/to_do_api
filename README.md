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

Requirements
============

To run this api code, you'll need to install the following libraries:

- django
- djangorestframework
- djangorestframework-jwt
- gunicorn
- django-heroku #this library is needed only if you wil deploy on heroku
- django-cors-headers

You can install these with the following command:

    pip install -r requirements.txt
