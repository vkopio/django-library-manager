from django.utils import timezone
from library_app.models import Book, Author, Genre, Reservation


def __time():
    return timezone.now()


def create_book(name='', isbn='', description=''):
    return Book.objects.create(
        name=name,
        isbn=isbn,
        description=description,
        pub_date=__time()
    )


def create_author(first_name='', last_name=''):
    return Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=__time()
    )


def create_genre(name=''):
    return Genre.objects.create(
        name=name,
    )


def create_reservation(**kwargs):
    return Reservation.objects.create(
        **kwargs
    )
