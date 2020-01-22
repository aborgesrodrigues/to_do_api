from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)

schema_view = get_swagger_view(title='APIs')

urlpatterns = [
    path('', schema_view),
    path('', include(router.urls)),
]
