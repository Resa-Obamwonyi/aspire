from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from ..models import User


# Test Get Favourites Endpoint
class TestGetFavourites(APITestCase):

    # create test user
    def setUp(self):
        self.data = {
            "username": "Theresa",
            "email": "theresaobamwonyi@gmail.com",
            "password": "resa12345",
        }
        self.user = User.objects.create(**self.data)

        self.token = f'Token {Token.objects.create(user=self.user).key}'
        self.login = {
            "email": "theresaobamwonyi@gmail.com",
            "password": "resa12345"
        }

    def test_get_favourites(self):
        response2 = self.client.get(reverse('favourites'), self.data, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


