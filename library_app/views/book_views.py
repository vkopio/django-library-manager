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


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['reservation_queue_position'] = user.libraryuser.reservation_queue_position(book=self.get_object())

        return context
