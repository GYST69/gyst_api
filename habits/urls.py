from django.urls import path, include
from .views import HabitListCreateView, HabitRetrieveUpdateDestroyAPIView
from .routers import router

urlpatterns = [
    # path("", HabitListCreateView.as_view(), name="habits"),
    # path("<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit_detail"),
    path("", include(router.urls))
]
