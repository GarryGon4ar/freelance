from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from task.models import Task
from task.serializers import TaskSerializer
from users.models import CustomUser


class TaskTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/task/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = CustomUser
        return User.objects.create_user(
            'user',
            email='user@test.com',
            password='test',
            user_type='customer'
        )

    def test_task_list(self):
        self.client.login(username="user", password="test")
        response = self.client.get(self.uri)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(response.data, serializer.data)

    def test_create_task(self):
        self.client.login(username="user", password="test")
        params = {
            "title": "bla",
            "description": "bla bla",
            "award": '250',
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.data['owner'], self.user.pk)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
    def test_create_task_dev(self):
        CustomUser.objects.create_user(
            'user1',
            email='test1@test.com',
            password='test1',
            user_type='developer'
        )
        params = {
            "title": "bla",
            "description": "bla bla",
            "award": '250',
        }
        self.client.login(username="user1", password="test1")
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_task_patch(self):
        self.client.login(username="user", password="test")
        params = {
            "title": "bla",
            "description": "bla bla",
            "award": '250',
        }
        response = self.client.post(self.uri, params)
        response = self.client.get(self.uri)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(response.data, serializer.data)