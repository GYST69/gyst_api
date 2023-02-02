from django.urls import path
from .views import (
    HabitListCreateView,
    HabitRetrieveUpdateDestroyAPIView,
    HabitInstanceListAPIView,
)

urlpatterns = [
    path("", HabitListCreateView.as_view(), name="habits"),
    path("<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit_detail"),
    path("instance/<str:completed_at>/", HabitInstanceListAPIView.as_view(), name="habit_instance_list",
    ),
]
