from django.urls import reverse
from library_app.tests.extended_test_case import ExtendedTestCase
from library_app.sample.utilities.factories import create_book
from library_app.models import Reservation


class ReservationViewTests(ExtendedTestCase):
    def setUp(self):
        self.book = create_book('test_book')
        self.login()

    def test_user_can_reserve_a_book(self):
        self.__post_reservation_create(self.book.id)

        reservation = Reservation.objects.last()

        self.assertEqual(reservation.reserver, self.user().libraryuser)
        self.assertEqual(reservation.book, self.book)
        self.assertEqual(self.response.status_code, 302)

    def test_user_cannot_reserve_the_same_book_twice(self):
        self.__post_reservation_create(self.book.id)
        self.__post_reservation_create(self.book.id)

        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(self.response.context['errors'], ['User has already reserved this book.'])

    def test_cannot_reserve_a_book_if_not_logged_in(self):
        self.logout()
        self.__post_reservation_create(self.book.id)

        self.assertEqual(Reservation.objects.count(), 0)

    def test_user_can_reserve_maximum_of_three_books(self):
        books = [
            self.book,
            create_book('test_book_2'),
            create_book('test_book_3'),
            create_book('test_book_4')
        ]

        for book in books:
            self.__post_reservation_create(book.id)

        self.assertEqual(Reservation.objects.count(), 3)
        self.assertEqual(self.response.context['errors'], ['User has reserved maximum number of books.'])

    def test_user_can_cancel_a_reservation(self):
        self.__post_reservation_create(self.book.id)
        self.assertEqual(Reservation.objects.count(), 1)

        self.__post_reservation_delete(self.book.id)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_should_get_404_if_trying_to_reserve_non_existent_book(self):
        self.__post_reservation_create(1337)

        self.assertEqual(self.response.status_code, 404)

    def test_should_get_404_if_trying_to_cancel_reservation_for_non_existent_book(self):
        self.__post_reservation_delete(1337)

        self.assertEqual(self.response.status_code, 404)

    def test_should_get_404_if_trying_to_cancel_a_non_existent_reservation(self):
        self.__post_reservation_delete(self.book.id)

        self.assertEqual(self.response.status_code, 404)

    def __post_reservation_create(self, book_id):
        url = reverse('library_app:reservation_create', args=(book_id,))
        self.response = self.client.post(url)

    def __post_reservation_delete(self, book_id):
        url = reverse('library_app:reservation_delete', args=(book_id,))
        self.response = self.client.post(url)
