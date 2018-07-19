from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from library_app.models import Book, LibraryUser
from ._base import BaseModel


class Reservation(BaseModel):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        unique=False
    )

    reserver = models.ForeignKey(
        LibraryUser,
        related_name='reserver',
        on_delete=models.CASCADE,
        unique=False
    )

    def clean(self):
        reserved_the_same_book = Reservation.objects.filter(reserver=self.reserver, book=self.book)
        reservation_count = Reservation.objects.filter(reserver=self.reserver).count()

        if reserved_the_same_book:
            raise ValidationError(_('You have already reserved this book.'))

        if reservation_count >= self.__max_reservation_count():
            raise ValidationError(_('You have reserved maximum number of books.'))

    def __str__(self):
        return self.book.name + ', reserver: ' + self.reserver.user.username

    @staticmethod
    def __max_reservation_count():
        return 3

    class Meta:
        ordering = ['creation_date']
