from django.shortcuts import render
from library_app.models import Book, Author, Genre


def index(request):
    context = {
        'book_count': Book.objects.all().count(),
        'author_count': Author.objects.all().count(),
        'genre_count': Genre.objects.all().count()
    }

    return render(request, 'library_app/index.html', context)
