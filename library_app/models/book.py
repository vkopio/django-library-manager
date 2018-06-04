from django.db import models
from django.urls import reverse
from library_app.validators import validate_isbn
from library_app.models import Author, Genre
from ._base import BaseModel


class Book(BaseModel):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, validators=[validate_isbn])
    description = models.TextField(blank=True)
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def reservations(self):
        from .reservation import Reservation
        return Reservation.objects.filter(book=self)

    def get_absolute_url(self):
        return reverse('library_app:book_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
