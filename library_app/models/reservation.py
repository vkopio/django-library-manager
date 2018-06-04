from django.db import models
from ._base import BaseModel
from .book import Book
from django.contrib.auth.models import User


class Reservation(BaseModel):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        unique=False
    )

    reserver = models.ForeignKey(
        User,
        related_name='reserver',
        on_delete=models.CASCADE,
        unique=False
    )

    def __str__(self):
        return self.book.name + ', reserver: ' + self.reserver.username

    class Meta:
        ordering = ['-creation_date']
