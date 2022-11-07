from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api import views


schema_view = get_schema_view(
   openapi.Info(
      title="APIs",
      default_version='v1',
      description="APIs tests"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'tasks', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
