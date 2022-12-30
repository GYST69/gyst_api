from django.urls import path

from .views import HabitCreateView

urlpatterns = [
    path("", HabitCreateView.as_view(), name="habit"),
    path("<int:id>", HabitCreateView.as_view(), name="habit_update"),
]
