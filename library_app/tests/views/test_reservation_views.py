from django.urls import reverse
from ..utils.extended_test_case import ExtendedTestCase
from library_app.tests.utils.factories import create_book
from library_app.models import Reservation


class BookViewTests(ExtendedTestCase):
    def setUp(self):
        self.book = create_book('test_book')

    def test_user_can_reserve_a_book(self):
        self.login()
        self.__post_reservation_create(self.book.id)

        reservation = Reservation.objects.last()

        self.assertEqual(reservation.reserver, self.user())
        self.assertEqual(reservation.book, self.book)
        self.assertEqual(self.response.status_code, 302)

    def test_user_cannot_reserve_the_same_book_twice(self):
        self.login()
        self.__post_reservation_create(self.book.id)
        self.__post_reservation_create(self.book.id)

        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(self.response.context['errors'], ['User has already reserved this book.'])

    def test_cannot_reserve_a_book_if_not_logged_in(self):
        self.__post_reservation_create(self.book.id)

        self.assertEqual(Reservation.objects.count(), 0)

    def test_user_can_reserve_maximum_of_three_books(self):
        books = [
            self.book,
            create_book('test_book_2'),
            create_book('test_book_3'),
            create_book('test_book_4')
        ]

        self.login()

        for book in books:
            self.__post_reservation_create(book.id)

        self.assertEqual(Reservation.objects.count(), 3)
        self.assertEqual(self.response.context['errors'], ['User has reserved maximum number of books.'])

    def __post_reservation_create(self, book_id):
        url = reverse('library_app:reservation_create', args=(book_id,))
        self.response = self.client.post(url)
