from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(
        max_length=25,
        null=False,
    )
    text = models.CharField(
        max_length=50,
    )
