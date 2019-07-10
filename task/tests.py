from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from task.models import Task
from task.serializers import TaskSerializer
from users.models import CustomUser


class TaskTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/api/v1/tasks/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        return CustomUser.objects.create_user(
            'user',
            email='user@test.com',
            password='test',
            user_type=1,
            balance='100',
            expenses='0'
        )

    def test_task_list(self):
        # checking if we get task list
        self.client.login(username="user", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_customer_create_task_(self):
        # checking if customer can create a task
        self.client.login(username="user", password="test")
        params = {
            "title": "bla",
            "description": "bla bla",
            "award": '100',
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code,201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_developer_create_task(self):
        CustomUser.objects.create_user(
            'user1',
            email='test1@test.com',
            password='test1',
            user_type=0
        )
        params = {
            "title": "bla",
            "description": "bla bla",
            "award": '250',
        }
        self.client.login(username="user1", password="test1")
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

