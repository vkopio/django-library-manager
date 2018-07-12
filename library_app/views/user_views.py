from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from library_app.models import Book


@login_required
def user_detail(request):
    user = request.user.libraryuser
    context = {
        'reservations': user.reservations,
        'borrowings': user.borrowings
    }

    return render(request, 'library_app/user_detail.html', context)
