from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.HabitCreateView.as_view(), name="habits"),
]