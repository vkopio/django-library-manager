from django.db import models
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

    def __str__(self):
        return self.book.name + ', reserver: ' + self.reserver.username

    class Meta:
        ordering = ['-creation_date']
