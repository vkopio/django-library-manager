from django.shortcuts import render
from django.views import generic

from .apps import app_dir
from .models import Book, Author, Genre


def index(request):
    context = {
        'book_count': Book.objects.all().count,
        'author_count': Author.objects.all().count,
        'genre_count': Genre.objects.all().count
    }

    return render(request, app_dir('index.html'), context)


class BookListView(generic.ListView):
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('name')
