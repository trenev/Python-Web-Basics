from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters!')


def validate_file_max_size_in_mb(image):
    limit_mb = 5
    file_size = image.file.size

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f'Max size of file is {str(limit_mb)} MB!')

