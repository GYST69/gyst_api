from rest_framework import generics
from .serializers import HabitSerializer, HabitInstanceSerializer, HabitLevelSerializer
from .models import Habit, HabitInstance, HabitLevel
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


class HabitLevelViewSets(viewsets.ModelViewSet):
    serializer_class = HabitLevelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Habit.objects.filter(account=self.request.user).filter(id=Habit.root_id)

class HabitInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = HabitInstanceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = HabitInstance.objects.all()
    filter_backends = [HabitInstanceFilterBackend]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
