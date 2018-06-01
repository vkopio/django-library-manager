from django.core.exceptions import ValidationError
from .sample.utilities.isbn import valid_isbn


def validate_isbn(value):
    if not valid_isbn(value):
        raise ValidationError('%s is not a valid ISBN number' % value)
