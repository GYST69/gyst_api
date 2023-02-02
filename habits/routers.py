from rest_framework import routers
from .views import HabitViewSet

router = routers.DefaultRouter()
router.register(r'', HabitViewSet)