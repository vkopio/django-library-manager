from django.shortcuts import render
from .apps import app_dir
from .models import Book, Author, Genre


def index(request):
    book_count = Book.objects.all().count
    author_count = Author.objects.all().count
    genre_count = Genre.objects.all().count

    context = {
        'book_count': book_count,
        'author_count': author_count,
        'genre_count': genre_count
    }

    return render(request, app_dir('index.html'), context)
