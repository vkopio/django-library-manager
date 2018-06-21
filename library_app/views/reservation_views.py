from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from library_app.models import Book, Reservation


@login_required
def reservation_create(request, book_id):
    book = Book.objects.get(pk=book_id)

    try:
        reservation = Reservation(book=book, reserver=request.user)
        reservation.full_clean()
        reservation.save()
    except ValidationError as error:
        context = {
            'book': book,
            'errors': error.messages
        }

        return render(request, 'library_app/index.html', context)

    return redirect(book)
