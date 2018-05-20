from django.db import models
from .author import Author
from .genre import Genre


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
