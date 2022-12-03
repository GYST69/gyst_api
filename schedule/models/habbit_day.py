from django.db import models
from schedule.models.habbit_abstract import Habbit


class DailyHabbit(models.Model):
    COLOR_CHOOSE=[
        '#0000CF',
        '#970000',
        '#FFFF18',
        '#007800',
    ]
    habbit = models.ForeignKey(Habbit, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    was_performed = models.BooleanField()
    color = models.CharField(max_length=7, choices=COLOR_CHOOSE)
