from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name',
    )

    age = models.IntegerField()

    profile_image = models.URLField(
        verbose_name='Link to Profile Image',
    )


class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    content = models.TextField()

    note_image = models.URLField(
        verbose_name='Link to Image',
    )
