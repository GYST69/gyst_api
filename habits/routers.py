from rest_framework import routers
from .views import HabitViewSet, HabitInstanceViewSet

habit_router = routers.DefaultRouter()
habit_instance_router = routers.DefaultRouter()

habit_router.register(r"", HabitViewSet)
habit_instance_router.register(r"", HabitInstanceViewSet)
