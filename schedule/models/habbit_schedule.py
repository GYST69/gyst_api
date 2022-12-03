from django.db import models
from schedule.models.habbit_day import DailyHabbit
from accounts.models import Account

class Schedule(models.Model):
    day = models.ForeignKey(DailyHabbit, on_delete=models.CASCADE)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
