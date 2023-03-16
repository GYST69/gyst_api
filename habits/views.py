from rest_framework import status
from .serializers import HabitSerializer, HabitInstanceSerializer
from .models import Habit, HabitInstance
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .filters import HabitInstanceFilterBackend
from rest_framework.response import Response
from datetime import datetime


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Habit.objects.all()

    def get_queryset(self):
        return Habit.objects.filter(account=self.request.user)

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class HabitInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = HabitInstanceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = HabitInstance.objects.all()
    filter_backends = [HabitInstanceFilterBackend]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        habit_id = request.data.get("habit_id")
        serializer.save(habit_id=habit_id)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
