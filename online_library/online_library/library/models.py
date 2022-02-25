from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    profile_image = models.URLField()


class Book(models.Model):
    BOOK_TITLE_MAX_LENGTH = 30
    BOOK_TYPE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=BOOK_TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    book_image = models.URLField()

    type = models.CharField(
        max_length=BOOK_TYPE_MAX_LENGTH,
    )

    class Meta:
        ordering = ['type', 'title']
