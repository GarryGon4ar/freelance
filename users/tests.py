from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from task.views import TaskList
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from users.models import CustomUser


class TestTaskList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.view = TaskList.as_view()
        self.uri = '/task/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = CustomUser
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "id": "1",
            "award": '250',
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))


    def test_user_login(self):
        response = self.client.post('/rest-auth/login/', {'username': 'test', 'email': 'testuser@test.com', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_user_not_exist(self):
        response = self.client.get('/users/555')
        self.assertEqual(response.status_code, 404)

