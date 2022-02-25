from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from furniture_store.web.validators import validate_min_price


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )


class Furniture(models.Model):
    type = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(4),
        ),
    )

    price = models.FloatField(
        validators=(
            validate_min_price,
        ),
    )

    model = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(4),
        ),
    )

    image = models.URLField()

    year = models.IntegerField(
        validators=(
            MinValueValidator(1950),
            MaxValueValidator(2050),
        ),
    )

    material = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    description = models.CharField(
        max_length=100,
        validators=(
            MinLengthValidator(10),
        ),
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('type', 'model', 'year')
