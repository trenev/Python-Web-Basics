from django.core.exceptions import ValidationError


def validate_time_value(value):
    if not value > 0:
        raise ValidationError('Time must be positive number!')
