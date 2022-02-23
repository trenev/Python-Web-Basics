from django.db import models


class Task(models.Model):
    OPEN = 'Open'
    IN_PROGRESS = 'In progress'
    COMPLETE = 'Complete'

    STATUSES = [(x, x) for x in (OPEN, IN_PROGRESS, COMPLETE)]

    title = models.CharField(
        max_length=30,
        verbose_name='Task',
    )

    description = models.CharField(
        max_length=150,
    )

    dead_line = models.DateField(
        verbose_name='Due Date',
    )

    status = models.CharField(
        max_length=max(len(x) for x, _ in STATUSES),
        default=OPEN,
    )
