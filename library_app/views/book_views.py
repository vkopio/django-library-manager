from django.db import connection
from django.views import generic
from library_app.models import Book


class BookListView(generic.ListView):
    context_object_name = 'books'
    paginate_by = 1

    def get_queryset(self):
        search = self.request.GET.get('search', False)

        if search and connection.vendor == 'postgresql':
            return Book.objects.filter(name__search=search)

        return Book.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search', '')

        if search:
            context['search_params'] = '&search=' + search

        return context


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['reservation_queue_position'] = user.libraryuser.reservation_queue_position(book=self.get_object())

        return context
