from django.db import models


class BookManager(models.Manager):
    def newest(self, limit=1):
        return self.order_by('-creation_date')[:limit]

    def most_borrowed(self, limit=1):
        return self.order_by('-borrowings_count')[:limit]
