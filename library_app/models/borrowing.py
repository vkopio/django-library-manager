from django.db import models
from library_app.models import Book, LibraryUser
from ._base import BaseModel


class Borrowing(BaseModel):
    due_date = models.DateField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    borrower = models.OneToOneField(LibraryUser, related_name='borrower', on_delete=models.SET_NULL, null=True)
    lender = models.OneToOneField(LibraryUser, related_name='lender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book.name + ', borrower: ' + self.borrower.username + ', due date: ' + str(self.due_date)
