from django.db import models
from ._base import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
