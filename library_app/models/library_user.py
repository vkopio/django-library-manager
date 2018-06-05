from django.contrib.auth.models import User


class LibraryUser(User):
    class Meta:
        proxy = True

    def reservations(self):
        from .reservation import Reservation
        return Reservation.objects.filter(reserver=self)
