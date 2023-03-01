from django.urls import path, include
from .routers import habit_router, habit_instance_router, habit_level_router

urlpatterns = [
    path("level/", include(habit_level_router)),
    path("instances/", include(habit_instance_router.urls)),
    path("", include(habit_router.urls)),
]
