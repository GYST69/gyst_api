from django.db import models


# Create your models here.

class Habbit(models.Model):

    HABBIT_CHOICES = [
        ('Good', 'good'),
        ('Bad', 'bad'),
    ]
    name = models.CharField(max_length=30)
    type = models.CharField(choices=HABBIT_CHOICES)
    creation_date = models.DateField()
    upgrade_date = models.DateField()
    additional_info = models.TextField(max_length=300)
    was_performed = models.BooleanField()
