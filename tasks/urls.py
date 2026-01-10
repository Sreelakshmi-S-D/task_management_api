from django.urls import path,include

from rest_framework.routers import DefaultRouter

from tasks.views import TasksViewSet,StatusViewSet

router = DefaultRouter()
app_name = 'tasks'

router.register(r'',TasksViewSet,basename='tasks')
router.register(r'status',StatusViewSet,basename='status')

urlpatterns = [
    path('', include(router.urls)),
]