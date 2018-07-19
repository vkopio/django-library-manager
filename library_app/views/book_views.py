from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.views import generic
from library_app.models import Book


class BookListView(generic.ListView):
    context_object_name = 'books'
    paginate_by = 20

    def get_queryset(self):
        search_params = self.request.GET.get('search', False)

        if search_params and connection.vendor == 'postgresql':
            return Book.objects.search_by_name(search_params)

        return Book.objects.all_by_name()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_params = self.request.GET.get('search', '')

        if search_params:
            context['search_params'] = '&search=' + search_params

        return context


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}

    if request.user.is_authenticated:
        context['reservation_queue_position'] = request.user.libraryuser.reservation_queue_position(book=book)

    return render(request, 'library_app/book_detail.html', context)
