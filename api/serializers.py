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


class StateTaskSerializer(serializers.BaseSerializer):
    """
    Class responsable for serializing the states
    """
    def to_representation(self, data):
        states = []
        for item in data:
            states.append({"value": item[0], "label": item[1]})
        return states