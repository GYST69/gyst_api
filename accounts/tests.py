from django.urls import reverse
from .models import Account
from rest_framework import status
from rest_framework.test import APITestCase


class AuthViewsTests(APITestCase):
    def setUp(self):
        self.email = "lemcio@mail.com"
        self.password = "eldote"
        self.data = {"email": self.email, "password": self.password}
        self.url = reverse("token_obtain_pair")
        self.user = Account.objects.create_user(
            email="lemcio@mail.com", password="eldote"
        )

    def test_register_user(self):
        data = {"email": "johan@johanveryhard.com", "password": "uhaveryhard12"}
        register_url = reverse("register_user")
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_user_is_active(self):
        self.assertEqual(self.user.is_active, 1)

    def test_user_is_not_superuser(self):
        self.assertEqual(self.user.is_superuser, 0)

    def test_user_is_not_anonymous(self):
        self.assertEqual(self.user.is_anonymous, 0)

    def test_user_is_not_staff(self):
        self.assertEqual(self.user.is_staff, 0)

    def test_user_obtain_JWT(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_unauthorized(self):
        response = self.client.post(
            self.url, {"email": "user@foo.com", "password": "pass"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
