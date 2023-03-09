from django.db import models
from accounts.models import Account
from colorfield.fields import ColorField
from rest_framework.validators import UniqueValidator
from colour import Color


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
    # do przemyslenia models.Caasscade
    habit_level = models.CharField(
        max_length=10, choices=LEVEL_CHOOICES, default="moderate"
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.root_id is not None:
            if self.habit_level == "easy":
                color_conversion = list(Color(self.color).get_hsl())
                color_conversion[2] =0.2
                color_conversion[1] =0.4
                self.color = color_conversion
            elif self.habit_level == "hard":
                color_conversion = list(Color(self.color).get_hsl())
                color_conversion[2] = 0.2
                color_conversion[1] = 0.4
                self.color = color_conversion
        super().save(force_insert, force_update, using, update_fields)


class HabitInstance(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-completed_at",)

    def __str__(self):
        return f"{self.habit.name} completed by {self.habit.account} on {self.completed_at}"
