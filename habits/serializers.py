from datetime import date
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import serializers
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
        habit_id = data["habit_id"]
        try:
            get_object_or_404(Habit, id=habit_id)
        except Http404:
            raise serializers.ValidationError("Habit not found with the given id")
        completed_at = data.get("completed_at", date.today())
        if HabitInstance.objects.filter(
            habit_id=habit_id, completed_at=completed_at
        ).exists():
            raise serializers.ValidationError("Habit already done this day")
        return data
