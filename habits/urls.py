from django.urls import path

from .views import HabitCreateView, HabitUpdateAPIView

urlpatterns = [
    path("", HabitCreateView.as_view(), name="habit_create"),
    path("<int:id>/", HabitUpdateAPIView.as_view(), name="habit_update"),
]
