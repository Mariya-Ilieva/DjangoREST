from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Please ensure this name contains only letters.')


def validate_phone_number(value):
    if not all(x.isdigit() for x in value):
        raise ValidationError('Please ensure this number contains only digits.')
