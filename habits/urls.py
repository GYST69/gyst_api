from django.urls import path

from .views import HabitCreateView

urlpatterns = [
    path("", HabitCreateView.as_view(), name="habits"),
]
