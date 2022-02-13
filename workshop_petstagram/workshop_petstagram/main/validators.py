from datetime import date

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters!')


def validate_file_max_size_in_mb(image):
    limit_mb = 5
    file_size = image.file.size

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f'Max size of file is {str(limit_mb)} MB!')


def validate_min_date(value):
    min_date = date(1920, 1, 1)

    if value < min_date:
        raise ValidationError(f'Date must be greater than {min_date}')


def validate_max_date(value):
    max_date = date.today()

    if value >= max_date:
        raise ValidationError(f'Date must be earlier than {max_date}')
