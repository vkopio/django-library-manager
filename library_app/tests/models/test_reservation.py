from library_app.tests.extended_test_case import ExtendedTestCase
from library_app.sample.utilities.factories import create_book, create_reservation


class AuthorTestCase(ExtendedTestCase):
    def setUp(self):
        self.book = create_book("test-book", "")
        self.reservation = create_reservation(book=self.book, reserver=self.user.libraryuser)

    def test_str_returns_desired_format(self):
        self.assertEqual(self.reservation.__str__(), "test-book, reserver: test_user")
