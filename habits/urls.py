from django.urls import path
from .views import HabitListCreateView, HabitRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", HabitListCreateView.as_view(), name="habits"),
    path("<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit_detail"),
]
