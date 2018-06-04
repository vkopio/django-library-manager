from django.db import models
from ._base import BaseModel
from .book import Book
from django.contrib.auth.models import User


class Borrowing(BaseModel):
    due_date = models.DateField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    borrower = models.OneToOneField(User, related_name='borrower', on_delete=models.SET_NULL, null=True)
    lender = models.OneToOneField(User, related_name='lender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book.name + ', borrower: ' + self.borrower.username + ', due date: ' + str(self.due_date)
