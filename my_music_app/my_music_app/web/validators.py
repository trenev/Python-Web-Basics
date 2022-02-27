from django.core.exceptions import ValidationError
import re


def validate_username_characters(value):
    pattern = "^[A-Za-z0-9_]*$"

    if not bool(re.match(pattern, value)):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

