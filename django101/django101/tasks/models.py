from django.db import models

# Create your models here.


class Schedule(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
    )
    description = models.CharField(
        max_length=100,
    )
    dead_line = models.DateField(
        auto_now=True,
    )

