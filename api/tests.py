from django.test import TestCase, Client

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse

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
        response = client.post("/users/", data={"name":"Daniel"})
        # get data from db
        user = User.objects.get(name="Daniel")
        serializer = UserSerializer(user, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        # get API response
        client = Client()
        response = client.put("/users/1/", data={"name":"Alessandro Borges"})
        # get data from db
        user = User.objects.get(pk=1)
        serializer = UserSerializer(user, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskTest(TestCase):

    def setUp(self):
        user = User.objects.create(name="Alessandro")
        Task.objects.create(user=user, description="Task 1", state="to_do")
        Task.objects.create(user=user, description="Task 2", state="to_do")

        user = User.objects.create(name="Rejane")
        Task.objects.create(user=user, description="Task 1.1", state="to_do")
        Task.objects.create(user=user, description="Task 2.2", state="to_do")

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

    def test_invalid_user(self):
        # get API response
        client = Client()
        response = client.get("/tasks/user/3/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

