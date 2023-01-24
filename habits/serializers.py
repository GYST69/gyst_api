from rest_framework import serializers
from .models import Habit, HabitInstance


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "name", "color", "description")


class HabitInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitInstance
        fields = ("id", "habit_id", "completed_at")
