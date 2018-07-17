from library_app.tests.extended_test_case import ExtendedTestCase
from library_app.models import LibraryUser
from library_app.sample.utilities.factories import create_book, create_reservation, create_borrowing
from django.contrib.auth.models import User


class GenreTestCase(ExtendedTestCase):
    def setUp(self):
        self.book = create_book("test-book", "")

    def test_library_user_borrowings_can_be_returned(self):
        borrowing = create_borrowing(book=self.book, borrower=self.user.libraryuser)

        self.assertEqual(list(self.user.libraryuser.borrowings()), [borrowing])

    def test_library_user_reservations_can_be_returned(self):
        reservation = create_reservation(book=self.book, reserver=self.user.libraryuser)

        self.assertEqual(list(self.user.libraryuser.reservations()), [reservation])

    def test_library_user_reservation_queue_position_is_0_if_not_in_queue(self):
        self.assertEqual(self.user.libraryuser.reservation_queue_position(self.book), 0)

    def test_library_user_reservation_queue_position_is_1_if_only_one_in_queue(self):
        create_reservation(book=self.book, reserver=self.user.libraryuser)

        self.assertEqual(self.user.libraryuser.reservation_queue_position(self.book), 1)

    def test_library_user_reservation_queue_position_is_2_if_makes_second_reservation(self):
        other_user = User.objects.create_user(
            username='test_user_2',
            password='test',
            email='test@test.test'
        )

        create_reservation(book=self.book, reserver=other_user.libraryuser)
        create_reservation(book=self.book, reserver=self.user.libraryuser)

        self.assertEqual(self.user.libraryuser.reservation_queue_position(self.book), 2)
