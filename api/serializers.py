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


class StateTaskSerializer(serializers.Serializer):
    """
    Class responsable for serializing the states
    """
    value = serializers.CharField()
    label = serializers.CharField()


class DetailSerializer(serializers.Serializer):
    detail = serializers.CharField()

class TaskUserSerializer(serializers.Serializer):
    """
    Class used for openapi documentation for a 400 HTTP response
    """
    user = serializers.ListField(child=serializers.CharField(), required=False)
    description = serializers.ListField(child=serializers.CharField(), required=False)
    state = serializers.ListField(child=serializers.CharField(), required=False)
