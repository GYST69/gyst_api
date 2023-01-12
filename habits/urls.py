from django.urls import path

from .views import HabitCreateView, HabitRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", HabitCreateView.as_view(), name="habit_create"),
    path("<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit_detail"),
]
