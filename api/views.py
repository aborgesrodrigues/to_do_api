from rest_framework import viewsets

from api.models import User, Task
from api.serializers import UserSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('description')
    serializer_class = TaskSerializer