from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
