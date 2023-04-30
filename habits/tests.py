from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Account, Habit
from django.contrib.auth import get_user_model
from .serializers import HabitSerializer


class TestAPIViews(APITestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create_user(
            email="user@email.com", password="1234", is_active=True
        )
        self.habit = Habit.objects.create(
            account=self.user, name="test", color="#abcdef", description="This is test"
        )

        self.habit_url_viewsets = reverse("habits-list")
        self.habit_url_viewsets_id = reverse(
            "habits-detail", kwargs={"pk": self.habit.id}
        )

        self.client.force_authenticate(user=self.user)
        self.serializer = HabitSerializer(instance=self.habit)

    def test_habit_create(self):
        data = {
            "account": self.user,
            "name": "test_create",
            "color": "#abcfff",
            "description": "This is test for create",
        }
        response = self.client.post(
            self.habit_url_viewsets,
            data,
        )
        habit_from_database = Habit.objects.filter(name="test_create").first()
        habit_from_database_serialized = HabitSerializer(instance=habit_from_database)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, habit_from_database_serialized.data)

    def test_habit_list(self):
        for habit_number in range(3):
            Habit.objects.create(
                account=self.user,
                name="test " + str(habit_number),
                color="#abcdef",
                description="This is test for list",
            )
        response = self.client.get(
            self.habit_url_viewsets,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Habit.objects.all()))

    def test_habit_retrieve(self):
        response = self.client.get(
            self.habit_url_viewsets_id,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.serializer.data)

    def test_habit_patch(self):
        data = {"description": "This is test for update"}
        response = self.client.patch(self.habit_url_viewsets_id, json=data)
        habit_from_database = Habit.objects.filter(name="test").first()
        habit_from_database_serialized = HabitSerializer(instance=habit_from_database)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, habit_from_database_serialized.data)

    def test_habit_delete(self):
        response = self.client.delete(
            self.habit_url_viewsets_id,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(Habit.objects.filter(id=self.habit.id, visible=False).exists())
