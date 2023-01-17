
from django.db import models


class Area(models.Model):
    title = models.CharField(max_length=50)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} {self.number}'