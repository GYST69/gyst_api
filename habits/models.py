from django.db import models
from accounts.models import Account
from colorfield.fields import ColorField


class Habit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    color = ColorField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class HabitInstance(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-completed_at",)

    def __str__(self):
        return f"{self.habit.name} completed by {self.habit.account} on {self.completed_at}"
