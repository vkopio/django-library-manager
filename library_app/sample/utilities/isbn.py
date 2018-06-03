from stdnum import isbn
from stdnum.exceptions import InvalidFormat


def valid_isbn(value):
    try:
        isbn.validate(value)
        return True

    except InvalidFormat:
        return False
