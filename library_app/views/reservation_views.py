from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from library_app.models import Book, Reservation


@login_required
def reservation_create(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    try:
        reservation = Reservation(book=book, reserver=request.user.libraryuser)
        reservation.full_clean()
        reservation.save()
    except ValidationError as error:
        context = {
            'book': book,
            'errors': error.messages
        }

        return render(request, 'library_app/book_detail.html', context)

    return redirect(book)


@login_required
def reservation_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reservation = get_object_or_404(Reservation, book=book, reserver=request.user.libraryuser)

    reservation.delete()

    return redirect(book)
