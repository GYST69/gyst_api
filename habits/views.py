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


class HabitInstanceListAPIView(generics.ListAPIView):
    serializer_class = HabitInstanceSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        date_getted_from_url = self.kwargs["completed_at"]
        queryset = HabitInstance.objects.filter(
            completed_at=date_getted_from_url
        ).filter(habit__account=self.request.user)
        return queryset
