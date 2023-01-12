from rest_framework import generics
from .serializers import HabitSerializer
from .models import Habit
from rest_framework.permissions import IsAuthenticated



class HabitCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Return the list of habits for the logged-in user
        return Habit.objects.filter(account=self.request.user)  

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


    