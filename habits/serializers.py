from rest_framework import serializers
from .models import Habit, HabitInstance


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "name", "color", "description")

class HabitInstanceSerializer(serializers.ModelSerializer):
    habit = HabitSerializer()
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = HabitInstance
        fields = ('id', 'habit', 'account', 'date')