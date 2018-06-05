from django.views import generic
from library_app.models import Book


class BookListView(generic.ListView):
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('name')


class BookDetailView(generic.DetailView):
    model = Book
