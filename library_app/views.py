from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .apps import app_dir
from .models import Book, Author, Genre, Reservation


def index(request):
    context = {
        'book_count': Book.objects.all().count(),
        'author_count': Author.objects.all().count(),
        'genre_count': Genre.objects.all().count()
    }

    return render(request, app_dir('index.html'), context)


class BookListView(generic.ListView):
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('name')


class BookDetailView(generic.DetailView):
    model = Book


@login_required
def book_reservation(request, book_id):
    book = Book.objects.get(pk=book_id)

    if True:
        reservation = Reservation(book=book, reserver=request.user)
        reservation.full_clean()
        reservation.save()

    return redirect(book)
