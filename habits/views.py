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
        serializer.save(habit_id=habit_id)