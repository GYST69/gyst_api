from datetime import date
from django.core.exceptions import ValidationError
from rest_framework import generics
from .serializers import HabitSerializer, HabitInstanceSerializer
from .models import Habit, HabitInstance
from rest_framework.permissions import IsAuthenticated


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Habit.objects.filter(account=self.request.user)

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class HabitRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Habit.objects.filter(account=self.request.user)


class HabitInstanceCreateView(generics.CreateAPIView):
    serializer_class = HabitInstanceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit_id = self.request.data.get("habit_id")
        completed_at = self.request.data.get("completed_at")
        if not completed_at:
            completed_at = date.today().strftime("%Y-%m-%d")
        habit_instance = HabitInstance.objects.filter(habit_id=habit_id, completed_at=completed_at)
        if habit_instance.exists():
            raise ValidationError("Habit instance already exists for this date")
        serializer.save(habit_id=habit_id)
