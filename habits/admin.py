from django.contrib import admin
from habits.models import Habit, HabitInstance


# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitInstance)