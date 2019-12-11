from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import User, Task
from api.serializers import UserSerializer, TaskSerializer, StateTaskSerializer


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

    @action(detail=False,
            methods=['get'],
            url_path='user/(?P<id_user>\d+)')
    def user_tasks(self, request, id_user):
        #Validate if id_user is informed
        if id_user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = None
        try:
            # Check if id of user is valid
            user = User.objects.get(pk= id_user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset = Task.objects.filter(user= user)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False,
            methods=['get'])
    def states(self, request):
        serializer = StateTaskSerializer(Task.STATE_OPTIONS)
        return Response(serializer.data)

    queryset = Task.objects.all().order_by('description')
    serializer_class = TaskSerializer