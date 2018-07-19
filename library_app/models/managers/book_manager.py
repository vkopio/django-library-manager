from django.db import models
from django.db.models import Count


class BookManager(models.Manager):
    def newest(self, limit=1):
        return self.order_by('-creation_date')[:limit]

    def most_borrowed(self, limit=1):
        return self.exclude(borrowings_count=0).order_by('-borrowings_count')[:limit]

    def all_by_name(self):
        return self.__with_related_objects().order_by('name')

    def search_by_name(self, search):
        return self.__with_related_objects().filter(name__search=search)

    def __with_related_objects(self):
        return self.annotate(Count('reservation')).prefetch_related('authors', 'genres', 'borrowing')
