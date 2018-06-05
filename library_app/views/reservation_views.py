from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from library_app.models import Book, Reservation


@login_required
def book_reservation(request, book_id):
    book = Book.objects.get(pk=book_id)

    if True:
        reservation = Reservation(book=book, reserver=request.user)
        reservation.full_clean()
        reservation.save()

    return redirect(book)
