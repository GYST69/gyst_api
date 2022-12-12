from django.db import models
from accounts.models import Account


# Create your models here.
class Habit(models.Model):
    COLOR_CHOOSE = [
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('green', 'Green')
    ]
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    color = models.CharField(choice=COLOR_CHOOSE, max_length=7)
    create_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_add=True)
    describtion = models.TextField(max_length=500)

    class Meta:
        ordering =('-create_date')
