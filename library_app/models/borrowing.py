from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from library_app.models import Book, LibraryUser
from ._base import BaseModel


class Borrowing(BaseModel):
    due_date = models.DateField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(LibraryUser, related_name='borrower', on_delete=models.SET_NULL, null=True)
    lender = models.ForeignKey(LibraryUser, related_name='lender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book.name + ', borrower: ' + self.borrower.user.username + ', due date: ' + str(self.due_date)


@receiver(post_save, sender=Borrowing)
def update_book_borrowings_count(sender, instance, **kwargs):
    book = instance.book
    book.borrowings_count += 1
    book.save()
