from django.urls import reverse
from .models import Habit, Account
from rest_framework.test import APITestCase
from rest_framework import status


class TestAPIViews(APITestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create_user(
            email="user@email.com",
            password='1234',

        )
        self.habit = Habit.objects.create(
            account=self.user,
            name="test",
            color="#abcdef",
            description="This is test"
        )
        self.habit_url_CreateAPIView = reverse("habit_create")
        self.habit_url_RetrieveUpdateDestroyAPIView = reverse("habit_update", kwargs={'id':self.habit.id})

    def test_habit_post(self):
        data = {
            "account": "1",
            "name": "test_create",
            "color": "#abcfff",
            "description": "This is test for create",
        }
        response = self.client.post(self.habit_url_CreateAPIView, data)
        self.client.cred
        self.assertEqual(response.status_code, status.HTTP_200_OK)
