from datetime import date
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import serializers
from .models import Habit, HabitInstance
from rest_framework.validators import UniqueTogetherValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "name", "color", "description", "root_id", "habit_level")

    def validate(self, attrs):
        root_id = attrs.get("root_id")
        habit_level = attrs.get("habit_level")
        if root_id is not None:
            queryset = Habit.objects.filter(root_id=root_id, habit_level=habit_level)
            if self.instance is not None:
                queryset = queryset.exclude(pk=self.instance.pk)
            if queryset.exists():
                raise serializers.ValidationError(
                    "Habit with this root_id and habit_level already exists."
                )
        return attrs


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
