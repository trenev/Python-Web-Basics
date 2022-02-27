from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import validate_username_characters


class Profile(models.Model):
    USER_NAME_MAX_LENGTH = 15
    USER_NAME_MIN_LENGTH = 2

    MIN_AGE = 0

    username = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USER_NAME_MIN_LENGTH),
            validate_username_characters,
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE),
        ),
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    MIN_PRICE = 0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_AND_B_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    GENRES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRES,
    )

    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['genre', 'artist', 'album_name']
