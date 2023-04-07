from django.db import models
from datetime import date
from accounts.models import Account
from colorfield.fields import ColorField
from rest_framework.validators import UniqueValidator


class Habit(models.Model):
    LEVEL_CHOOICES = (
        ("easy", "easy"),
        ("moderate", "moderate"),
        ("hard", "hard"),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    color = ColorField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500, blank=True)
    root_id = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.DO_NOTHING
    )
    habit_level = models.CharField(
        max_length=10, choices=LEVEL_CHOOICES, default="moderate"
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class HabitInstance(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateField(default=date.today)

    class Meta:
        ordering = ("-completed_at",)
        unique_together = ("habit", "completed_at")

    def __str__(self):
        return f"{self.habit.name} completed by {self.habit.account} on {self.completed_at}"
