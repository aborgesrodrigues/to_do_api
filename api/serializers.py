from rest_framework import serializers

from api.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    """
    Class responsable for serializing the user object
    """
    class Meta:
        model = User
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    """
    Class responsable for serializing the task object
    """
    class Meta:
        model = Task
        fields = ['id', 'user', 'description', 'state']