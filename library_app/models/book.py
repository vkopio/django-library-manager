from django.db import models
from ._base import BaseModel

from .author import Author
from .genre import Genre


class Book(BaseModel):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
