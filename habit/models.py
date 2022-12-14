from django.db import models
from accounts.models import Account
from colorfield.fields import ColorField
import datetime
# Create your models here.
class Habit(models.Model):
    TIME_CHOOSE=[
            (datetime.time(hour=x, minute=y), "{}:{}".format(x,y)) for x in range(0,24) for y in [0,30]]
    COLOR_CHOOSE = [
        ("#0000FF", "Blue"),
        ("#FF0000", "Red"),
        ("#FFFF00", "Yellow"),
        ("#008000", "Green"),
    ]
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    # color = models.CharField(choices=COLOR_CHOOSE, max_length=7)
    color = ColorField(choices=COLOR_CHOOSE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    start_time = models.DurationField(choices=TIME_CHOOSE, null=True)
    finish_time = models.DurationField(choices=TIME_CHOOSE, null=True)
    class Meta:
        ordering = ("-create_date",)

    def __str__(self):
        return self.name

# Kolor powinien oznaczać priorytet nawyku
# zielony - wypada zrobic
# czerwony - Musisz!
# żółty - urgent