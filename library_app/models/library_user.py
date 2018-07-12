from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ._base import BaseModel


class LibraryUser(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def borrowings(self):
        from .borrowing import Borrowing
        return Borrowing.objects.filter(borrower=self)

    def reservations(self):
        from .reservation import Reservation
        return Reservation.objects.filter(reserver=self)

    def reservation_queue_position(self, book):
        from .reservation import Reservation
        reservations = Reservation.objects.filter(book=book)

        for i, reservation in enumerate(reservations):
            if reservation.reserver == self:
                return i + 1

        return 0


@receiver(post_save, sender=User)
def create_library_user(sender, instance, created, **kwargs):
    if created:
        LibraryUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_library_user(sender, instance, **kwargs):
    instance.libraryuser.save()
