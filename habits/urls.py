from django.urls import path
from .views import HabitListCreateView, HabitRetrieveUpdateDestroyAPIView, HabitInstanceCreateView

urlpatterns = [
    path("", HabitListCreateView.as_view(), name="habits"),
    path("<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit_detail"),
    path('instance/', HabitInstanceCreateView.as_view(), name='habit_instance_create')
]
