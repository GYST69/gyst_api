from rest_framework import serializers
from .models import Habit, HabitInstance, HabitLevel


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "name", "color", "description")


class HabitLevelSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = HabitLevel
        fields = '__all__'

class HabitInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitInstance
        fields = ("id", "habit_id", "completed_at")
