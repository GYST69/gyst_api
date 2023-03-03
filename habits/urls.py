from django.urls import path, include
from .routers import habit_router, habit_instance_router

urlpatterns = [
    path("instances/", include(habit_instance_router.urls)),
    path("", include(habit_router.urls)),
]
