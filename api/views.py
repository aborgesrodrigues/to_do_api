from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import User, Task
from api.serializers import UserSerializer, TaskSerializer, StateTaskSerializer, DetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        """
        API endpoint that retrieve all users
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        API endpoint that create a user
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("User not Found", DetailSerializer )})
    def retrieve(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific user
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("User not Found", DetailSerializer )})
    def update(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific user
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("User not Found", DetailSerializer )})
    def partial_update(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific user
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("User not Found", DetailSerializer )})
    def destroy(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific user
        """
        return super().destroy(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    def list(self, request, *args, **kwargs):
        """
        API endpoint that retrieve all tasks
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(responses={400: "User not found"})
    def create(self, request, *args, **kwargs):
        """
        API endpoint that create a task
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("Task not found", DetailSerializer )})
    def retrieve(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific task
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("Task not found", DetailSerializer ),
                                    400: "User not found"})
    def update(self, request, *args, **kwargs):
        """
        API endpoint that update a specific task
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("Task not Found", DetailSerializer ),
                                    400: "User not found"})
    def partial_update(self, request, *args, **kwargs):
        """
        API endpoint that retrieve a specific task
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("Task not Found", DetailSerializer )})
    def destroy(self, request, *args, **kwargs):
        """
        API endpoint that delete a specific task
        """
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(responses={404: openapi.Response("User not found", DetailSerializer )})
    @action(detail=False,
            methods=['get'],
            url_path='user/(?P<id_user>\d+)')
    def user_tasks(self, request, id_user):
        """
        API endpoint that list all tasks por a specific user
        """

        #Validate if id_user is informed
        if id_user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = None
        try:
            # Check if id of user is valid
            user = User.objects.get(pk= id_user)
        except User.DoesNotExist:
            return Response(data={ "detail": "Not found." }, status=status.HTTP_404_NOT_FOUND)
        queryset = Task.objects.filter(user= user)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: openapi.Response("", StateTaskSerializer)})
    @action(detail=False,
            methods=['get'])
    def states(self, request):
        """
        API endpoint that list all possible states for the tasks
        """

        serializer = StateTaskSerializer(Task.STATE_OPTIONS)
        return Response(serializer.data)

    queryset = Task.objects.all().order_by('description')
    serializer_class = TaskSerializer