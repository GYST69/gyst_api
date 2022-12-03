from django.db import models

class Habbit(models.Model):
    name = models.CharField(max_length=30)
    creation_date = models.DateField()
    upgrade_date = models.DateField()
    additional_info = models.TextField(max_length=300)


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
