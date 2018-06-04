from django.db import models
from django.urls import reverse
from library_app.validators import validate_isbn
from ._base import BaseModel

from .author import Author
from .genre import Genre


class Book(BaseModel):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, validators=[validate_isbn])
    description = models.TextField(blank=True)
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse('library_app:book_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
