from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Account, Habit
from django.contrib.auth import get_user_model


class TestAPIViews(APITestCase):
    def setUp(self) -> None:

        self.user = Account.objects.create_user(
            email="user@email.com", password="1234", is_active=True
        )
        self.habit = Habit.objects.create(
            account=self.user, name="test", color="#abcdef", description="This is test"
        )
        self.habit_url_ListCreateAPIView = reverse("habits")
        self.habit_url_DetailAPIView = reverse(
            "habit_detail", kwargs={"pk": self.habit.id}
        )
        self.client.force_authenticate(user=self.user)

    def test_authenticated_habit_retrieve(self):
        habit_data = {
            "id": self.habit.id,
            "name": "test",
            "color": "#abcdef",
            "description": "This is test",
        }

        response = self.client.get(
            self.habit_url_DetailAPIView,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, habit_data)

    def test_authenticated_habit_create(self):
        data = {
            "account": self.user,
            "name": "test_create",
            "color": "#abcfff",
            "description": "This is test for create",
        }

        response = self.client.post(
            self.habit_url_ListCreateAPIView,
            data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_habit_patch(self):
        data = {"description": "This is test for update"}
        response = self.client.patch(self.habit_url_DetailAPIView, data)
        description_field = Habit.objects.filter(name="test").values("description")[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(description_field, data)

    def test_authenticated_habit_delete(self):
        response = self.client.delete(
            self.habit_url_DetailAPIView,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())

    def test_authenticated_habit_list(self):
        for habit_number in range(4):
            Habit.objects.create(
                account=self.user,
                name="test " + str(habit_number),
                color="#abcdef",
                description="This is test for list",
            )
        response = self.client.get(
            self.habit_url_ListCreateAPIView,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Habit.objects.all()))
