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

        if reserved_the_same_book:
            raise ValidationError(_('User has already reserved this book.'))

    def __str__(self):
        return self.book.name + ', reserver: ' + self.reserver.username

    class Meta:
        ordering = ['-creation_date']
