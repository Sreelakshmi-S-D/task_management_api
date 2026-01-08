from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from tasks.models import Task
from tasks.constants import STATUS_PENDING,STATUS_COMPLETED

# Create your tests here.
class TaskModelTest(TestCase):

    def test_task_creation_default_status(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, STATUS_PENDING)

    def test_task_with_completed_status(self):
        task = Task.objects.create(title="Completed Task", status=STATUS_COMPLETED)
        self.assertEqual(task.status, STATUS_COMPLETED)
        self.assertEqual(task.title, "Completed Task")

    def test_task_string_representation(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(str(task), "Test Task")

class TaskAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = "/api/tasks/"

    def test_create_task_success(self):
        data = {"title": "API Task"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["result"], "success")
        self.assertEqual(Task.objects.count(), 1)

    def test_create_task_invalid_status(self):
        data = {
            "title": "Invalid Task",
            "status": "WrongStatus"
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["result"], "failure")
        self.assertIn("status", response.data["errors"])

    def test_list_tasks(self):
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], "success")
        self.assertEqual(len(response.data["records"]), 2)
