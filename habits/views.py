from rest_framework import generics
from .serializers import HabitSerializer, HabitInstanceSerializer
from .models import Habit, HabitInstance
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

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
    filterset_fields = ["completed_at"]


    def get_queryset(self):
        return HabitInstance.objects.filter(account=self.request.user)
