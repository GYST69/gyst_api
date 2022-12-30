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
        self.response = self.client.post(self.url, self.data, format="json")
        self.token = self.response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT {0}".format(self.token))

    def test_user_is_active(self):
        self.assertEqual(self.user.is_active, 1, "Active User")

    def test_user_is_not_superuser(self):
        self.assertEqual(self.user.is_superuser, 0)

    def test_user_is_not_anonymous(self):
        self.assertEqual(self.user.is_anonymous, 0)

    def test_user_is_not_staff(self):
        self.assertEqual(self.user.is_staff, 0)

    def test_user_obtain_JWT(self):
        self.assertEqual(
            self.response.status_code, status.HTTP_200_OK, self.response.content
        )

    def test_user_is_autheticated(self):
        self.assertEqual(self.user.is_authenticated, 1)

    def test_user_is_unauthorized(self):
        response = self.client.post(
            self.url, {"email": "user@foo.com", "password": "pass"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
