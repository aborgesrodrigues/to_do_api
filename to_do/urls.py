from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api import views
from to_do.views import users

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('client/users', users)
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
