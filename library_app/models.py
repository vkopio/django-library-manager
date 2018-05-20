from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
