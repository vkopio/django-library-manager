from django.contrib.auth.models import User


class LibraryUser(User):
    class Meta:
        proxy = True

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


def as_library_user(user):
    if user.__class__.__name__ != 'User':
        return None

    user.__class__ = LibraryUser
    return user
