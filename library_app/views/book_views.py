from django.views import generic
from library_app.models import Book


class BookListView(generic.ListView):
    context_object_name = 'books'
    paginate_by = 20

    def get_queryset(self):
        return Book.objects.order_by('name')


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['reservation_queue_position'] = user.libraryuser.reservation_queue_position(book=self.get_object())

        return context
