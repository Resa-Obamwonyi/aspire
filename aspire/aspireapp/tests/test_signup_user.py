from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Test User Signup Endpoint
class TestSignupUser(APITestCase):
    def setUp(self):
        self.data = {
            "username": "Theresa",
            "email": "theresaobamwonyi@gmail.com",
            "password": "resa12345",
        }

    def test_signup_user(self):
        url = reverse('signup')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

