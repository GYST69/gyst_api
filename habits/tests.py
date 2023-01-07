from django.urls import reverse
from .models import Habit, Account
from rest_framework.test import APITestCase
from rest_framework import status


class TestAPIViews(APITestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create_user(
            email="user@email.com",
            password='1234',
            is_active=True

        )
        self.habit = Habit.objects.create(
            account=self.user,
            name="test",
            color="#abcdef",
            description="This is test"
        )
        self.data_user= {
            "email":"user@email.com",
                    "password":'1234',

        }
        self.habit_url_CreateAPIView = reverse("habit_create")
        self.habit_url_RetrieveUpdateDestroyAPIView = reverse("habit_update", kwargs={'id':self.habit.id})
        self.token_obtain_url = reverse("token_obtain_pair")


    def test_habit_get(self):
        token_response = self.client.post(self.token_obtain_url, self.data_user, format="json")
        token = token_response.data["access"]
        response = self.client.get(self.habit_url_RetrieveUpdateDestroyAPIView,
                                    )
    def test_habit_post(self):
        data = {
            "account": self.user,
            "name": "test_create",
            "color": "#abcfff",
            "description": "This is test for create",
        }

        token_response = self.client.post(self.token_obtain_url, self.data_user, format="json")
        token = token_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT {0}".format(token))
        auth_dict = { "HTTP_AUTHORIZATION":"JWT {0}".format(token)}
        response = self.client.post(self.habit_url_CreateAPIView,
                                    data,
                                    **auth_dict,
                                    )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
