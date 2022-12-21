from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Habit
        fields = [
            "id",
            "name",
            "color",
            "account",
            "description",
            "created_at",
            "updated_at",
        ]
