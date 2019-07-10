from _decimal import Decimal

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from users.models import CustomUser


class TestUser(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/api/v1/users/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        return CustomUser.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test',
            user_type=1,
        )

    def test_create_user(self):
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'user_type': 0,
            'balance': 100,
        }

        response = self.client.post(self.uri, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['user_type'], data['user_type'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': ''
        }

        response = self.client.post(self.uri, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_users_list(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_user_login(self):
        response = self.client.post('/api/v1/rest-auth/login/',
                                    {'username': 'test', 'email': 'testuser@test.com', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_user_not_exist(self):
        self.client.login(username="test", password="test")
        response = self.client.get('/api/v1/users/555')
        self.assertEqual(response.status_code, 404)
