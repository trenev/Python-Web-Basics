from django.db import models

# Create your models here.


class Task(models.Model):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETE = 3

    title = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.CharField(
        max_length=150,
    )

    dead_line = models.DateField(
        auto_now_add=True
    )

    status = models.IntegerField(
        choices=(
            (OPEN, 'Open'),
            (IN_PROGRESS, 'In progress'),
            (COMPLETE, 'Complete'),
        ),
        default=OPEN,
    )
