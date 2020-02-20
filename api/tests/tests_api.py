from django.test import TestCase, Client

# Create your tests here.
from rest_framework import status

from api.models import User, Task
from api.serializers import UserSerializer, TaskSerializer


class UserTest(TestCase):

    def setUp(self):
        User.objects.create(name="Alessandro")
        User.objects.create(name="Rejane")
        User.objects.create(name="Agatha")

    def test_get_all_users(self):
        # get API response
        client = Client()
        response = client.get("/users/")
        # get data from db
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_insert_user(self):
        # get API response
        client = Client()
        response = client.post("/users/", data={"name": "Daniel"})
        # get data from db
        user = User.objects.get(name="Daniel")
        serializer = UserSerializer(user, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        # get API response
        client = Client()
        response = client.put("/users/1/", data={"name": "Alessandro Borges"}, content_type="application/json")

        user = User.objects.get(name="Alessandro Borges")

        self.assertEqual(user.pk, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        # get API response
        client = Client()
        response = client.delete("/users/1/")

        user = User.objects.filter(pk=1)

        self.assertEqual(user.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_user(self):
        # get API response
        client = Client()
        response = client.get("/users/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TaskTest(TestCase):

    def setUp(self):
        user = User.objects.create(name="Alessandro")
        Task.objects.create(user=user, description="Task 1", state="to_do")
        Task.objects.create(user=user, description="Task 2", state="to_do")

        user = User.objects.create(name="Rejane")
        Task.objects.create(user=user, description="Task 1.1", state="to_do")
        Task.objects.create(user=user, description="Task 2.2", state="to_do")

        User.objects.create(name="Agatha")

    def test_insert_task(self):
        # get API response
        client = Client()
        response = client.post("/tasks/", data={"user": 3, "description": "Task 1.1.1", "state": "to_do"})
        # get data from db
        task = Task.objects.get(description="Task 1.1.1")
        serializer = TaskSerializer(task, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        # get API response
        client = Client()
        response = client.put("/tasks/2/", data={"user": 3, "description": "Task 1.1.1", "state": "done"}, content_type="application/json")

        task = Task.objects.get(pk=2)

        self.assertEqual(task.state, "done")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        # get API response
        client = Client()
        response = client.delete("/tasks/1/")

        task = Task.objects.filter(pk=1)

        self.assertEqual(task.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_tasks(self):
        # get API response
        client = Client()
        response = client.get("/tasks/")
        # get data from db
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_tasks_by_user(self):
        # get API response
        client = Client()
        response = client.get("/tasks/user/1/")
        # get data from db
        tasks = Task.objects.filter(user__pk=1)
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_task(self):
        # get API response
        client = Client()
        response = client.get("/tasks/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_user(self):
        # get API response
        client = Client()
        response = client.get("/tasks/user/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)