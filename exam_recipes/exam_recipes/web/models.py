from django.db import models

from exam_recipes.web.validators import validate_time_value


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
    )

    cooking_time = models.IntegerField(
        validators=(
            validate_time_value,
        ),
    )

    def __str__(self):
        return f'{self.title}'
