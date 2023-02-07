from datetime import date
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Habit, HabitInstance


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "name", "color", "description")


class HabitInstanceSerializer(serializers.ModelSerializer):
    habit_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = HabitInstance
        fields = ("id", "habit_id", "completed_at")

    def validate(self, data):
        print(data)
        habit_id = data["habit_id"]
        completed_at = data.get("completed_at", date.today())
        if HabitInstance.objects.filter(
            habit_id=habit_id, completed_at=completed_at
        ).exists():
            raise serializers.ValidationError("Habit already done this day")
        return data
