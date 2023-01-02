from rest_framework import generics
from .serializers import HabitSerializer
from .models import Habit
from rest_framework.permissions import IsAuthenticated


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class HabitRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Habit.objects.filter(account=self.request.user)
