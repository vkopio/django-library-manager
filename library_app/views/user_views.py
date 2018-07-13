from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_detail(request):
    user = request.user.libraryuser
    context = {
        'reservations': user.reservations,
        'borrowings': user.borrowings
    }

    return render(request, 'library_app/user_detail.html', context)
