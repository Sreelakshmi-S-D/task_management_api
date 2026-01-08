from django.urls import path,include

from rest_framework.routers import DefaultRouter

from tasks.views import TasksViewSet

router = DefaultRouter()
app_name = 'tasks'

router.register(r'',TasksViewSet,basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
