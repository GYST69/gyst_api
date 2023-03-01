from rest_framework import routers
from .views import HabitViewSet, HabitInstanceViewSet,HabitLevelViewSets

habit_router = routers.DefaultRouter()
habit_instance_router = routers.DefaultRouter()
habit_level_router = routers.DefaultRouter()

habit_router.register(r"", HabitViewSet, basename="habits")
habit_instance_router.register(r"", HabitInstanceViewSet)
habit_level_router.register(r"", HabitLevelViewSets)
