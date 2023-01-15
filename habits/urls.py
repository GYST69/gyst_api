from django.urls import include, path
from .views import HabitListCreateView

urlpatterns = [
    path("", HabitListCreateView.as_view(), name="habits"),
]