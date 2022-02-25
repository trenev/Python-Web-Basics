from django.core.exceptions import ValidationError


def validate_min_price(value):
    if value <= 0:
        raise ValidationError('Price must be positive number!')
