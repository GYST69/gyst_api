from django.db import models

class Habbit(models.Model):
    name = models.CharField(max_length=30)
    creation_date = models.DateField()
    upgrade_date = models.DateField()
    additional_info = models.TextField(max_length=300)

    class Meta:
        abstract = True
